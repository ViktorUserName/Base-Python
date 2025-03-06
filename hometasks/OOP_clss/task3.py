from logging import raiseExceptions


class Car:
    def __init__(self, color: str, item_type: str, year: int):
        self.__color = color
        self.__item_type = item_type
        self.__year = year

    @staticmethod
    def start_the_car():
        print('Машину завели')
    @staticmethod
    def turn_off_the_car():
        print('Машину заглушили')

    def set_color(self, color: str):
        try:
            if not isinstance(color, str):
                raise TypeError('Цвет должен быть строкой')
            self.__color = color
        except TypeError as e:
            print(f"Ошибка: {e}")

    def set_type(self, item_type: str):
        try:
            if not isinstance(item_type, str):
                raise TypeError('Тип должен быть строкой')
            self.__item_type = item_type
        except TypeError as e:
            print(f"Ошибка: {e}")

    def set_year(self, year: int):
        try:
            if not isinstance(year, int):
                raise TypeError('Год должен быть числом')
            self.__year = year
        except TypeError as e:
            print(f"Ошибка: {e}")

    def get_all(self):
        print(self.__color, self.__item_type, self.__year)

audi = Car('black','a4',2022)
audi.get_all()
audi.set_color('red')
audi.get_all()
audi.start_the_car()
audi.turn_off_the_car()

audi.set_color(22)
audi.get_all()
