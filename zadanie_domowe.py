bazaUzytkownikow = []

while True:
    a = input("1. Dodaj użytkownika \n2. Zobacz dane użytkownika \n3. Wyświetl wszyskie imiona użytkowników \n4. Wyjście \n")
    if a == "1":
        imie = input("Imie: ")
        email = input("Email: ")
        wiek = input("Wiek: ")
        uzytkownik = {
            "imie": imie,
            "email": email,
            "wiek": wiek
        }
        bazaUzytkownikow.append(uzytkownik)
    elif a == "2":
        kto = input("Użytkownik: ")
        for i in bazaUzytkownikow:
            if i["imie"] == kto:
                print(i)
    elif a == "3":
        for i in bazaUzytkownikow:
            print(i["imie"])
    elif a == "4":
        break
    else:
        print("Error 404: not found")
    print("\n")