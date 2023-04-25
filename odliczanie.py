import time
import random

def odliczanie(n):
    time.sleep(1)
    print('\033[1;' + str(random.randint(31, 36)) + 'm' + str(n-1))
    if n-1 > 1:
        odliczanie(n-1)

a = int(input("Podaj liczbe: "))
odliczanie(a)