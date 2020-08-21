import math
import numpy as np
from nltk.stem import PorterStemmer
# while True:
#     a = input('Please enter command: ')
#     if a == 'stop':
#         break
#     test_list = []
#     test_dic = {1: 2, 3:1}
#     test_list.append(1)
#     print(test_list)
#     print(math.log(8))
#     x = [1, 2, 3]
#     y = [4, 5, 6]
#     print(np.dot(np.array(x), np.array(y)))
# query = [1, 2, 3]
# for i in query[:len(query)]:
#     query.append(i+1)
# print(query)
# is_expanded = False
# while True:
#     if not is_expanded:
#         query = input('\nPlease input query: ')
#         if query == 'stop':
#             break
#         query_list = query.split(' ')
#         is_expanded = True
#     else:
#         print(query_list)
ps = PorterStemmer()
word_porter = ps.stem('good')
word_porter1 = ps.stem('golf')
word_porter2 = ps.stem('game')
print(word_porter)
print(word_porter1)
print(word_porter2)
