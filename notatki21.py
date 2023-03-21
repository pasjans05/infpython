# znaki ze stringa:

str = "abcdef"

print(str[2]) # only third

print(str[2:]) # third onwards

print(str[2::-2]) # from third to the beginning in reverse order


# listy:

letters = ["a", "b", "c"] # lista
leters = ("a", "b", "c") # tuple - krotka
matrix = [[0, 11], [2, 3]]  # tablica
zeros = [0] * 5
combined = zeros + letters

numbers = list(range(20))
chars = list("Hello World!")

x = "123"
y = int(input("podaj wiek"))


# listy 2:

numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 34]
first, *other, last = numbers

first = numbers[0]
other = numbers[0:-1]
last = numbers[-1]


# listy 3:

letters = ["a", "b", "c"]

for idx, letter in enumerate(letters):
    print(idx, letter)

for letter in enumerate(letters):
    print(letter)


# Given a list of numbers, unpack the values into individual variables.
# Then, compute and print the sum of those numbers

numbers = [3, 7, 9, 12]
one, two, three, four = numbers
# one = numbers[0]
# two = numbers[1]
# three = numbers[2]
# four = numbers[3]
print(one+two+three+four)


# min wartość:

def minimalnaW(numers):
    for idx, numer in enumerate(numers):
        if idx == 0:
            n = numer
        if numer < n:
            n = numer
    return n


numbers = (12, 3, 9, 8, 78, 22, 5, 4)
print(minimalnaW(numbers))


# lista krotek:

items = [("Product 1", 123),
         ("Product 2", 12),
         ("Product 3", 8123)]

# def sortItem(n):
#     return n[1]
# items.sort(key = sortItem)

items.sort(key = lambda n:n[1])
print(items)


# function to find the youngest student from a set [("jan", 20)]

students = [
    {"imie": "Jan", "wiek": 20},
    {"imie": "Karolina", "wiek": 15},
    {"imie": "Brunhilda", "wiek": 185}
]

students.sort(key = lambda n:n["wiek"])
print(students[0]["imie"])


# zwracanie tylko cen

items = [
    ("Product 1", 123),
    ("Product 2", 12),
    ("Product 3", 8123)
]

x = list(map(lambda item: item[1], items))

print(x)