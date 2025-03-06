

def imt () -> float | str:
    massa: int = int(input('Введите свою массу тела '))
    height: float = float(input('Введите свой рост '))
    try:
        if height <= 0 or height > 2.43 or massa <= 0 or massa > 200:
            raise Exception('Некорректные данные')
        index = massa/height**2
        if index <= 18:
            print('мало веса')
        if  18.0 < index < 25:
            print('хороший вес')
        if index >= 25:
            print('излишний вес')
        return round(index, 1)

    except ZeroDivisionError:
        return 'На ноль делить нельзя'



print(imt())