import numpy as np
import gensim
from konlpy.tag import Twitter
import pickle

twiiter = Twitter()
word2vec_model = gensim.models.Word2Vec.load('word2vec-model')
keyword_set = []
number_to_word_dic = {} #숫자를 집어넣으면 단어가 나옴
word_to_number_dic = {} #단어를 집어넣으면 순서가 나옴
with open('number_to_word_dic', 'rb') as handle:
    number_to_word_dic = pickle.load(handle)
with open('word_to_number_dic', 'rb') as handle:
    word_to_number_dic = pickle.load(handle)
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
    manu_word = twiiter.pos(word)
    manu_word = str(manu_word).replace("'", '').replace("(", '').replace(" ", '')
    manu_word = str(manu_word).replace("]", '').replace("[", '').replace(")", '').replace(",", '/')

    return manu_word

def manufacture_word2(word):
    manu_word = str(word).replace("'", '').replace("(", '').replace(" ", '')
    manu_word = str(manu_word).replace("]", '').replace("[", '').replace(")", '').replace(",", '/')

    return manu_word

if __name__ == "__main__":
    init()

    file = open("example.txt", 'r')

    exmaple = file.readline()
    TDM = np.zeros([WORD_NUM,1])

    exmaple_set = twiiter.pos(exmaple)
    for word in exmaple_set:
        try:
            TDM[int(word_to_number_dic[str(manufacture_word2(word))])][0] += 1.
        except:
            print(str(manufacture_word2(word)))

    weight_matrix = np.load("Weight_matrix.npy")

    result = weight_matrix.dot(TDM)
    max_index = result.argmax()

    print("분류 결과는 : ", keyword_set[max_index] , " 입니다")
