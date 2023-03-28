x = [1, 2, 3, 4]
#y = [1, 3, 6, 10]
y = []
def sumuj(i, n):
    if n < 0:
        return 0
    y[i] += x[n]
    sumuj(i, n-1)

for n in range(0, len(x)):
    y.append(x[n])
    sumuj(n, n-1)

print(y)