import os


path = os.getcwd()

dict_marks = {}

with open(os.path.join(path,'text.txt'), 'r', encoding='utf-8') as text_file:
    data = text_file.read()

lines = data.splitlines()

for i, line in enumerate(lines):
    line = line.split(' ')
    dict_marks[line[0]] = line[1]

new_string = ''
for key, value in dict_marks.items():
    value = int(value)
    if value <= 3:
        new_string += key + ' '  + str(value) + '\n'

print(new_string)