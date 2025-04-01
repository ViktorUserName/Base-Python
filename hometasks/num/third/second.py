import math


def credit():
    p = float(input('Какую процентную ставку предлагают (годовых, %)? '))
    s = float(input('Какую сумму хотите занять? '))
    n = int(input('Срок кредита в месяцах? '))

    p=p/(12*100)
    y = (s*p*(1+p)**n)/(1+p)**n-1
    bank_salary = y*n
    overpay = bank_salary-s
    print(f'Ежемесячная выплата {y:.2f}',f'Всего заплатите банку {bank_salary:.2f}',
          f'Переплата составит {overpay:.2f}',sep='\n')

credit()