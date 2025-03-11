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
class Bus:
    def __init__(self, v, max_v, max_sit, list_passenger, flag, dict_sit):
        self.v = v
        self.max_v = max_v
        self.max_sit = max_sit
        self.list_passenger = []
        self.flag = True
        dict_sit = {}

    def gaz(self, value):
        self.v = min(self.max_v, self.v + value)

