# Класс «Автобус». Класс содержит свойства:
# ● скорость
# ● максимальное количество посадочных мест
# ● максимальная скорость
# ● список фамилий пассажиров
# ● флаг наличия свободных мест
# ● словарь мест в автобусе
# Методы:
# ● посадка и высадка одного или нескольких пассажиров
# ● увеличение и уменьшение скорости на заданное значение
# ● операции in, += и -= (посадка и высадка пассажира по
# фамилии
from collections import OrderedDict

class Bus:
    def __init__(self, max_v, max_sit):
        self.v = 0
        self.max_v = max_v
        self.max_sit = max_sit
        self.list_passenger = []
        self.seat_map = OrderedDict()
        self.flag = True

    def change_speed(self, delta, silent=False):
        self.v = max(0, min(self.max_v, self.v + delta))
        if not silent:
            print(f"Скорость → {self.v} км/ч")

    def sitting(self, *names):
        for name in names:
            if len(self.list_passenger) < self.max_sit:
                sit_num = len(self.list_passenger) + 1
                self.list_passenger.append(name)
                self.seat_map[sit_num] = name
            else:
                print('Авторбус полный')
        self.flag = len(self.list_passenger) < self.max_sit

    def leave(self, *names):
        for name in names:
            if name in self.list_passenger:
                self.list_passenger.remove(name)
                seat_to_remove = next(k for k, v in self.seat_map.items() if v == name)
                del self.seat_map[seat_to_remove]
                print(f"{name} покинул автобус.")
            else:
                print(f"Пассажир {name} не найден.")

        self.flag = len(self.list_passenger) < self.max_sit

    def __contains__(self, name):
        """Проверка пассажира в автобусе"""
        return name in self.list_passenger

    def __iadd__(self, name):
        """Добавление пассажира через '+=' """
        self.sitting(name)
        return self

    def __isub__(self, name):
        """Высадка пассажира через '-=' """
        self.leave(name)
        return self

    def __str__(self):
        """Строковое представление автобуса"""
        return (f"Скорость: {self.v} км/ч (Макс: {self.max_v} км/ч)\n"
                f"Занято мест: {len(self.list_passenger)}/{self.max_sit}\n"
                f"Пассажиры: {', '.join(self.list_passenger) if self.list_passenger else 'Автобус пуст'}\n"
                f"Свободные места: {'Есть' if self.flag else 'Нет'}")


bus = Bus(max_v=120, max_sit=5)

bus.sitting('Петя', 'Вася')
bus.change_speed(20)
print(bus)