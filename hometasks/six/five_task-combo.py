# Используя map() и reduce() посчитать площадь
# квартиры, имея на входе характеристики комнат квартиры.
# Пример входных данных:

from functools import reduce
rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3}
]


def s_rooms (arr: list):
    list_of_s = list(map(lambda x: x['length'] * x['width'], arr))
    s_flat = reduce(lambda acc, x: acc + x, list_of_s)
    print(f"Общая площадь квартиры: {s_flat}")

s_rooms(rooms)