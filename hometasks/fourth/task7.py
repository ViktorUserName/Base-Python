list_binor = [5, 6, 7, 1, 2, 3, 4]

def binor_search(arr, num):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return print(mid)

        if arr[left] <= arr[mid]:
            if arr[left] <= num < arr[mid]:
                right = mid -1
            else:
                left = mid +1
        else:
            if arr[mid] < num <= arr[right]:
                left = mid +1
            else:
                right= mid -1
    return -1

binor_search(list_binor, 7)
