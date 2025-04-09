# Программа получает на вход число. Реализовать
# функцию, которая определяет, является ли это число простым
# (делится только на единицу и на само себя).

def simple_num (num):
    if num < 2:
        return "Число не простое"
    mid = num // 2

    while mid > 1:
        if num%mid == 0:
            return "Число не простое"
        mid = mid-1

    return 'число простое'

print(simple_num(2))
print(simple_num(3))
print(simple_num(5))
print(simple_num(7))
print(simple_num(11))
print(simple_num(6))