arrr = [1,2,3,4,5,6]

def binor(arr, num):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return -1

binor(arrr, 4)