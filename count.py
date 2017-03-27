from sobamchan_jp_preprocessor import Parser
from sobamchan_vocabulary import Vocabulary
from sobamchan_utility import Utility
util = Utility()

if __name__ == '__main__':
    parser = Parser()

    data = util.load_json('./data/result.json')

    s = list(filter(lambda d:d['talker'] == 's', data))
    y = list(filter(lambda d:d['talker'] == 'y', data))

    s_parsed_sentences = parser([d['content'] for d in s])
    y_parsed_sentences = parser([d['content'] for d in y])

    s_vocab = Vocabulary()
    y_vocab = Vocabulary()

    for s_parsed_sentence in s_parsed_sentences:
        s_vocab.new(s_parsed_sentence)
    for y_parsed_sentence in y_parsed_sentences:
        y_vocab.new(y_parsed_sentence)

    for i, count in s_vocab.counts.most_common(10):
        print(s_vocab.i2w[i], count)
    print('---')
    for i, count in y_vocab.counts.most_common(10):
        print(y_vocab.i2w[i], count)
