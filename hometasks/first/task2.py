import time

def wordPrinterBytime(word):
    for i in word:
        print(i, end='', flush=True)
        time.sleep(0.2)


word = "'Python' — лучший язык!"

wordPrinterBytime(word)
