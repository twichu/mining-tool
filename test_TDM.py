import numpy as np
import gensim
from konlpy.tag import Twitter
import re

twiiter = Twitter()
word2vec_model = gensim.models.Word2Vec.load('word2vec-model')
keyword_set = []
number_to_word_dic = {} #숫자를 집어넣으면 단어가 나옴
word_to_number_dic = {} #단어를 집어넣으면 순서가 나옴
KEYWORD_NUM = 45
WORD_NUM = 981586

def init():
    file = open("keyword.txt", "r")
    temp_set = file.readline()
    file.close()
    temp_set = temp_set.split(",")
    for word in temp_set:
        keyword_set.append(manufacture_word(word))

def manufacture_word(word):
    manu_word = str(word).replace("'", '').replace("(", '').replace(" ", '')
    manu_word = str(manu_word).replace("]", '').replace("[", '').replace(")", '').replace(",", '/')

    return manu_word

if __name__ == "__main__":
    init()

    number = 0
    for word in word2vec_model.wv.vocab:
        word_to_number_dic[word] = str(number)
        number_to_word_dic[str(number)] = word
        number += 1
    file = open("example.txt", 'r')
    exmaple = file.readline()
    TDM = np.full([WORD_NUM,1], 0)

    exmaple_set = twiiter.pos(exmaple)
    for word in exmaple_set:
        try:
            TDM[int(word_to_number_dic[str(manufacture_word(word))])][0] += 1.
        except:
            print("haha")

    weight_matrix = np.load("Weight_matrix.npy")

    result = weight_matrix.dot(TDM)
    max_index = result.argmax()

    print("분류 결과는 : ", keyword_set[max_index] , " 입니다")

    print(result)
    print(max_index, "값은 ", result[max_index])

    # for keyword_num in range(KEYWORD_NUM):
    #     for word_number in range(WORD_NUM):
    #         try:
    #             weight_matrix[keyword_num][word_number] = word2vec_model.similarity(keyword_set[keyword_num], number_to_word_dic[str(word_number)])
    #         except:
    #             weight_matrix[keyword_num][word_number] = 0
    #
    #     print(keyword_set[keyword_num], " 끝")
    #
    # np.save("Weight_matrix.npy", weight_matrix)