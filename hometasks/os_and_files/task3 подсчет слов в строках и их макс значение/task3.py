import os
import re


path = os.getcwd()
file = os.path.join(path,'text_example.txt')

with open(file, 'r', encoding='utf-8') as text_file:
    data = text_file.read()

dict_sum = {}

lines = data.splitlines()

for i, line in enumerate(lines):
    words = re.findall(r'\b\w+\b', line.lower())
    dict_sum[i] = {}
    for word in words:
        dict_sum[i][word] = dict_sum[i].get(word, 0) + 1

for i, words in dict_sum.items():
    most_frequent_word = max(words, key=words.get)
    print(f"Строка {i+1}: {most_frequent_word} ({words[most_frequent_word]})")

