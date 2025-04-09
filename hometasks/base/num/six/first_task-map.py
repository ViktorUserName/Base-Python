# Дан список чисел. С помощью map() получить список,
# где каждое число из исходного списка переведено в строку.
# Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]

nums_list = [1,3,4,5,6,7]

print(map(lambda x: x**2, nums_list))
def type_change (arr: list) -> list:
    return list(map(lambda item: str(item), arr))

print(type_change(nums_list))
