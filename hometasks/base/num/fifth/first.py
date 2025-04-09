# Дан список чисел, отсортированных по возрастанию.
# На вход принимается значение, равное одному из элементов
# списка. Реализовать функцию, выполняющую рекурсивный
# алгоритм бинарного поиска, на выходе программа должна
# вывести позицию искомого элемента в исходном списке.

nums = [1,2,3,4,5,6]

def search_position (num, arr):

    def binor(left, right):
        if left > right:
            return -1

        mid = (left+right)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return binor(mid+1, right)
        else:
            return binor(left, mid-1)

    return binor(0, len(arr) -1)

print(search_position(2,nums))