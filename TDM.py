import numpy as np
import gensim
from konlpy.tag import Twitter
import pickle

twiiter = Twitter()
keyword_set = []
number_to_word_dic = {} #숫자를 집어넣으면 단어가 나옴
word_to_number_dic = {} #단어를 집어넣으면 순서가 나옴
with open('number_to_word_dic', 'rb') as handle:
    number_to_word_dic = pickle.load(handle)
with open('word_to_number_dic', 'rb') as handle:
    word_to_number_dic = pickle.load(handle)
file = open("keyword", "r",encoding='utf8')
temp_set = file.readlines()
file.close()
KEYWORD_NUM = 0
for word in temp_set:
    KEYWORD_NUM += 1
WORD_NUM = 981586
weight_matrix = np.load("Weight_matrix.npy")

def init():
    file = open("keyword", "r",encoding='utf8')
    temp_set = file.readlines()
    file.close()
    for word in temp_set:
        keyword_set.append(manufacture_word(word).replace("\n", ""))

def manufacture_word(word):
    manu_word = twiiter.pos(word)
    manu_word = str(manu_word).replace("'", '').replace("(", '').replace(" ", '')
    manu_word = str(manu_word).replace("]", '').replace("[", '').replace(")", '').replace(",", '/')

    return manu_word

def manufacture_word2(word):
    manu_word = str(word).replace("'", '').replace("(", '').replace(" ", '')
    manu_word = str(manu_word).replace("]", '').replace("[", '').replace(")", '').replace(",", '/')

    return manu_word

def twitter_to_keyword(twitter_str):
    TDM = np.zeros([WORD_NUM, 1])
    twiiter_set = twiiter.pos(twitter_str)
    for word in twiiter_set:
        try:
            TDM[int(word_to_number_dic[str(manufacture_word2(word))])][0] += 1.
        except:
            pass
    result = weight_matrix.dot(TDM)
    max_index = result.argmax()
    keyword = keyword_set[max_index].replace(")", "").replace("(", "").replace("/Noun", "")

    return keyword

def user_extract_keyword(twitter_list):
    keyword_set=[]
    for twitter_str in twitter_list:
        keyword_set.append(twitter_to_keyword(twitter_str))

    num_list = []
    keyword_list = []
    for keyword in keyword_set:
        try:
            index = keyword_list.index(keyword)
            num_list[index] += 1
        except:
            keyword_list.append(keyword)
            num_list.append(int(1))
    num_list = np.array(num_list)
    top3_keyword = []
    for i in range(3):
        max_index = num_list.argmax()
        num_list[max_index] = 0
        top3_keyword.append(keyword_list[max_index])
    return top3_keyword