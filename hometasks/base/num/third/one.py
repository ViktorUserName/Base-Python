import math

def math_a ():
    a = int(input('Введите число a '))
    b = int(input('Введите число b '))
    y = (a**2//3)+(a**2+4)//b+(math.sqrt(a**2+4))//4+math.sqrt((a**2+4)**3)//4
    return print(y)
math_a()

def math_b ():
    x = int(input('Введите число x '))
    y = math.cos(x)+math.sin(x)
    return print(y)

math_b()

def math_c ():
    x = int(input('Введите число x '))
    y = (math.cos(x ** 2) ** 2 + math.sin(2 * x - 1) ** 2) ** (1 / 3)
    return  print(y)
math_c()

def math_d ():
    x = int(input('Введите число x '))
    y = 5*x+3*x**2*math.sqrt(1+math.sin(x)**2)
    return  print(y)

math_d()