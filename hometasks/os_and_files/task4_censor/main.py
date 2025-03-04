import os

def censor_func (text):
    path = os.getcwd()
    file = os.path.join(path, text)
    stop_file = os.path.join(path, 'stop_words.txt')

    with open(file, 'r', encoding='utf-8') as text_file:
        data = text_file.read().lower()

    with open(stop_file, 'r', encoding='utf-8') as text_file:
        censor = text_file.read().split(' ')

    for item in censor:
        star = len(item)
        data = data.replace(item, f'{star*'*'}')

    print(data)

censor_func('text.txt')