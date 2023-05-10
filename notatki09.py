# random:

import random
for i in range(10):
    print(random.random())

# randrange:

import random
i = 0
while True:
    x = random.randrange(0,100)
    i += 1
    if x == 77:
        print("wylosowales 77 za ", i ,"razem")
        break

# losowanie uczniow:

import random

kl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (0, 14):
    x = random.randint(0, 14)
    kl[x] += 1

m = 0

for n in range (0, 14):
    if kl[n] > m:
        m = kl[n]
        l = n

print("najczęściej losowany był numer ", l+1, ", był losowany ", m, "razy")

