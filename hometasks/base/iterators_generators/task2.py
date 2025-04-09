def over_digit (num_of_dig):
    while True:
      for i in range(1, num_of_dig):
          yield i


for n in over_digit(5):
    print(n, end='-')
