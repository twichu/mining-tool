import numpy as np
import gensim
from konlpy.tag import Twitter
import pickle

twiiter = Twitter()
word2vec_model = gensim.models.Word2Vec.load('word2vec-model')
keyword_set = []
number_to_word_dic = {} #숫자를 집어넣으면 단어가 나옴
word_to_number_dic = {} #단어를 집어넣으면 순서가 나옴
file = open("keyword", "r",encoding='utf8')
temp_set = file.readlines()
file.close()
KEYWORD_NUM = 0
for word in temp_set:
    KEYWORD_NUM += 1
WORD_NUM = 981586

def init():
    file = open("keyword", "r",encoding='utf8')
    temp_set = file.readlines()
    file.close()
    for word in temp_set:
        keyword_set.append(manufacture_word(word).replace("\n", ""))

def manufacture_word(word):
    manu_word = twiiter.pos(word)
    manu_word = str(manu_word).replace("'", "").replace("(", "").replace(" ", "")
    manu_word = str(manu_word).replace("]", "").replace("[", "").replace(",", "/").replace(")", "")

    return manu_word

if __name__ == "__main__":
    init()
    weight_matrix = np.zeros([KEYWORD_NUM, WORD_NUM])

    number = 0
    for word in word2vec_model.wv.vocab:
        word_to_number_dic[word] = str(number)
        number_to_word_dic[str(number)] = word
        number += 1

    count = 0
    for keyword_num in range(KEYWORD_NUM):
        for word_number in range(WORD_NUM):
            try:
                weight_matrix[keyword_num][word_number] = word2vec_model.similarity(keyword_set[keyword_num], number_to_word_dic[str(word_number)])
            except:
                weight_matrix[keyword_num][word_number] = 0
        count += 1
        print(count, keyword_set[keyword_num], float("{0:.1f}".format((count / KEYWORD_NUM) * 100)), "%...")

    np.save("Weight_matrix.npy", weight_matrix)

    with open('keyword_set.pickle', 'wb') as handle:
        pickle.dump(keyword_set, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('number_to_word_dic', 'wb') as handle:
        pickle.dump(number_to_word_dic, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('word_to_number_dic', 'wb') as handle:
        pickle.dump(word_to_number_dic, handle, protocol=pickle.HIGHEST_PROTOCOL)
