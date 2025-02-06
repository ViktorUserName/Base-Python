group_numbers = [-1,2,-3,44,323,421,65,78,4,5,6]

def quik_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [item for item in arr if item>pivot]
    middle = [item for  item in arr if item==pivot]
    right = [item for item in arr if item< pivot]

    return quik_sort(left)+middle+quik_sort(right)

print(quik_sort(group_numbers))
