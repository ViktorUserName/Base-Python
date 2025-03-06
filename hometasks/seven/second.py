
def calculate () -> int | float | str:
    a = int(input('введите первое число '))
    b = int(input('введите второе число '))
    operator = input('введите оператор сложения (+) вычитания (-) деления(/) и умножения (*) ')
    try:
        result = eval(f'{a}{operator}{b}')
    except ValueError:
        return 'Ошибка: Введите числовые значения'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    return result if str(result)[-1] != '0' else round(result)




print(calculate())