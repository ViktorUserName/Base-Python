# Дан список чисел. С помощью filter() получить список
# тех элементов из исходного списка, значение которых
# больше 0.

nums_list = [2,4,22,-21,0,-100,112]

def positive_list (arr: list) -> list:
    return list(filter(lambda item: item>0, nums_list))

print(positive_list(nums_list))