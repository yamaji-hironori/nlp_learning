# -----------------------------------------------------------------------------
# nega_posi
# 2021/02/28
# -----------------------------------------------------------------------------
import codecs
import csv
import os
import re
from natto import MeCab

__location__ = \
        os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))


def getNegaPosiDic():
    negaPosiDic = {}
    for i_csv in ['./dataset/yougen.csv', './dataset/noun.csv']:
        with codecs.open(os.path.join(__location__, i_csv), 'r', 'utf-8') \
                                                                       as f_in:
            reader = csv.reader(f_in, delimiter=',', lineterminator='\n')
            for x in reader:
                y = x[0].split(" ")
                negaPosiDic[y[1]] = y[0]

    return negaPosiDic


def nlp(data):
    points = 0
    nm = MeCab()
    negaposi_dic = getNegaPosiDic()
    sentenses = re.split('[。！!♪♫★☆>?？（）w]', data)
    try:
        for sentense in sentenses:
            negaposi = 0
            result_all = nm.parse(sentense)
            result_words = result_all.split('\n')[:-1]

            for word in result_words:
                try:
                    word_toarray = re.split('[\t,]', word)
                    if word_toarray[7] in negaposi_dic:
                        negaposi = int(negaposi_dic[word_toarray[7]])
                        print(word_toarray[7], negaposi_dic[word_toarray[7]], \
                            flush=True)
                except Exception as e:
                    print('%r' % e, flush=True)
            points += negaposi

    except Exception as e:
        print('%r' % e, flush=True)
        print(data, flush=True)

    return points


if __name__ == '__main__':
    data = '美味しく炊けました。臭くなくてとても良いですね。大満足の一品です！'
    print(nlp(data))
