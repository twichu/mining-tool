import pickle

# test_dir = {}
#
# for i in range(100):
#     test_dir[str(i) + "호오"] = i
#
# with open('filename.pickle', 'wb') as handle:
#     pickle.dump(test_dir, handle, protocol=pickle.HIGHEST_PROTOCOL)
b= {}

with open('number_to_word_dic', 'rb') as handle:
    number_to_word_dic = pickle.load(handle)

print(number_to_word_dic[str(4)])