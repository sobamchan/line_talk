import re

import sobamchan_utility
util = sobamchan_utility.Utility()

def cut_header(raw_data):
    return raw_data[3:]

def is_date(line):
    ptn = u'^\d+\/\d+\/\d+'
    return re.match(ptn, line) != None

def is_another_line(line):
    '''
    check if line is connected from previous line
    '''
    return len(line.split('\t')) == 1

def separate_line(line):
    '''
    {'talker', 'content'}
    '''
    date, talker, content = [d.strip() for d in line.split('\t')]
    return {'talker': talker, 'content': content}

def parse_line(line):
    '''
    [{'talker', 'content'}]
    '''
    if not is_date(line) and is_another_line(line):
        return line.strip()
    if not is_date(line):
        return separate_line(line)
    else:
        return None

def parse(raw_data):
    raw_data = cut_header(raw_data)
    talks = []
    for line in raw_data:
        try:
            parsed_line = parse_line(line)
            if parsed_line == None:
                continue
            if type(parsed_line) == type(str()):
                talks[len(talks)-1]['content'] += parsed_line
            elif parsed_line != None:
                talks.append(parsed_line)
        except:
            pass

    return talks

if __name__ == '__main__':
    raw_data = util.readlines_from_filepath('./data/line.txt')
    talks = parse(raw_data)
    util.save_json(talks, './data/result.json')
