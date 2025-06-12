# import time
# from multiprocessing import cpu_count, Process
# from threading import Thread
#
# def factorial(n: int) -> int:
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
# def heavy_computation(n):
#     factorial(n)
#
# def first_check():
#     n = 8
#     numbers = [50000 + i for i in range(n)]
#
#     start = time.time()
#     results = []
#     for num in numbers:
#         results.append(factorial(num))
#     end = time.time()
#
#     print(f"Время (последовательно): {end - start:.2f} сек")
#
# def thread_check():
#     n = 8
#     numbers = [50000 + i for i in range(n)]
#     threads = []
#
#     start = time.time()
#     for num in numbers:
#         t = Thread(target=heavy_computation, args=(num,))
#         t.start()
#         threads.append(t)
#
#     for t in threads:
#         t.join()
#
#     end = time.time()
#     print(f"Время (многопоточность): {end - start:.2f} сек")
#
# def process_check():
#     n = cpu_count()  # число логических ядер
#     numbers = [50000 + i for i in range(n)]
#     processes = []
#
#     start = time.time()
#     for num in numbers:
#         p = Process(target=heavy_computation, args=(num,))
#         p.start()
#         processes.append(p)
#
#     for p in processes:
#         p.join()
#
#     end = time.time()
#     print(f"Время (многопроцессность): {end - start:.2f} сек")
#
# if __name__ == "__main__":
#     first_check()
#     thread_check()
#     process_check()

import socket

host = '178.62.234.8'
port = 6379

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)  # 5 секунд на подключение

try:
    sock.connect((host, port))
    print("✅ Порт открыт, подключение успешно.")
except socket.error as e:
    print(f"❌ Порт закрыт или недоступен: {e}")
finally:
    sock.close()