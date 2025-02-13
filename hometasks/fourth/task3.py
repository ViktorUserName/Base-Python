def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)