# Сделать декоратор, который измеряет время,
# затраченное на выполнение декорируемой функции.
import time

def time_dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,*kwargs)
        end_time = time.time()
        print(f'Время = {func.__name__}: {end_time-start_time:.4f} сек')
        return result
    return wrapper

@time_dec
def long_f(summ=0):
    while summ < 100000000:
        summ +=2

long_f()
