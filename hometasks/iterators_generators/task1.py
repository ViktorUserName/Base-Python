def fibon(enddig):
    a, b = 0, 1
    while a < enddig:
        yield a
        a, b = b, a+b

test = fibon(100)

for num in test:
    print(num, end=' ')