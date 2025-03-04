import os
import re

path = os.getcwd()

with open(os.path.join(path,'text.txt'), 'r', encoding='utf-8') as text_file:
    data = text_file.read()

numbers = re.findall(r'\d+', data)
summary = sum(map( lambda x: int(x), numbers))
print(summary)