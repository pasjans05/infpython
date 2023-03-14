def FizBuz():
    j = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
            j += 1
        elif i % 5 == 0:
            i = "Buzz"
        elif i % 3 == 0:
            i = "Fizz"
            j += 1
        print(i)
    return j

print("liczb podzielnych przez 3: ", FizBuz())