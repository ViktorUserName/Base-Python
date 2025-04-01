llist = [1,2,3,4,5,43,3,2,3,4]

def summ(arr):
    summary = 0
    i = 0
    while i!=len(arr):
        summary= summary+arr[i]
        i+=1
    print(f'сумма {summary}, max {max(arr)} min {min(arr)}')


summ(llist)