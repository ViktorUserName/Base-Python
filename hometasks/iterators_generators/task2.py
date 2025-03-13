def over_digit (num_of_dig):
    # start = 1
    while True:
      for i in range(1, num_of_dig):
          yield i
      # start += 1


for n in over_digit(5):
    print(n, end='-')
