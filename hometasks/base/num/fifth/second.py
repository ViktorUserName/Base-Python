# Программа получает на вход число в десятичной
# системе счисления. Реализовать функцию, которая
# переводит входное число в двоичную систему счисления.
# Допускается реализация функции как в рекурсивном
# варианте, так и с итеративным подходом.

num = 23

def decoder_nums(target):
    if target == 1:
        return 1

    if target % 2 == 1:
        return  int(str(decoder_nums(target // 2)) + str(1))
    else:
        return int(str(decoder_nums(target // 2)) + str(0))


print(decoder_nums(num))
