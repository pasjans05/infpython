# liczby parzyste:

i = 0
parz = 1
while (parz < 10):
    if parz % 2 == 0:
        i += 1
        print(f"liczba: {parz}")
    parz += 1
print(f"liczb parzystych: {i}")

# funkcje:

def print_name(first_name, last_name, age = 18):
    print(f"Twoje imie to: {first_name} {last_name} of age: {age}")

print_name("asdsadf", "sssss")

# funkcje 2:

def greet(name):
    print(f"Hi {name}")
    return True
print(greet("Staszek"))

# krotka:

def multiply(*numbers):
    print(type(numbers))
multiply(2, 3, 4, 5)

# słownik:

def save_user(**user):
    print (user)
save_user(id = 2, name = "Filip")

# multiply:

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total
print(multiply(2, 3, 4, 5))
