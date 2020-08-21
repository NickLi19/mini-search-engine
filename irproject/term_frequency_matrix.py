import io
import json

word_dic_full = {}
for line in io.open("words_porter.json", 'r', encoding='utf-8'):
    new_line = line.replace('\n', '').replace('\r', '').strip()
    if new_line != '':
        word_dic = json.loads(new_line)
        for key in word_dic.keys():
            if key != '*sequence*':
                if key not in word_dic_full:
                    word_dic_full[key] = [0 for _ in range(40)]
                    word_dic_full[key][word_dic['*sequence*']-1] += word_dic[key]
                else:
                    word_dic_full[key][word_dic['*sequence*']-1] += word_dic[key]

file = io.open('Words_Frequency_Matrix_porter.txt', 'a', encoding='utf-8')
# number_of_words = len(word_dic_full.keys())
# file.write('Number of words: {}'.format(str(number_of_words)))
# file.write('\n')
# print('Number of words: {}'.format(str(number_of_words)))
#
# print('-----------------------------------')
# print('Term Frequency Matrix: ')
# file.write('Term Frequency Matrix: ')
# file.write('\n')
count_dic = {}
for item in word_dic_full.keys():
    count_dic[item] = sum(word_dic_full[item])
    data = '{}: {}'.format(item, word_dic_full[item])
    file.write(data)
    file.write('\n')
#     print('{}: {}'.format(item, word_dic_full[item]))
#
# print('-----------------------------------')
# print('20 Most Frequent Words with Document Frequency: ')
# file.write('20 Most Frequent Words with Document Frequency: ')
# file.write('\n')
# count_dic_new = sorted(count_dic.items(), key=lambda d: d[1], reverse=True)
# for items in count_dic_new[:20]:
#     key = items[0]
#     df = 40 - word_dic_full[key].count(0)
#     file.write('{}: {}'.format(key, str(df)))
#     file.write('\n')
#     print('{}: {}'.format(key, str(df)))
# file.close()
