bazaUzytkownikow = []
while True:
    a = input("1. Dodaj użytkownika \n2. Zobacz dane użytkownika \n3. Wyświetl wszyskie imiona użytkowników \n4. Usuń użytkownika \n5. Wyjście \n")
    if a == "1": # dodaje uzytkownika
        imie = input("Imie: ")
        email = input("Email: ")
        wiek = input("Wiek: ")
        uzytkownik = {
            "imie": imie,
            "email": email,
            "wiek": wiek
        }
        bazaUzytkownikow.append(uzytkownik)
    elif a == "2": # wyswietla dane uzytkownika
        kto = input("Użytkownik: ")
        for i in bazaUzytkownikow:
            if i["imie"] == kto:
                print(i)
    elif a == "3": # wyswietla imiona wszystkich uzytkownikow
        for i in bazaUzytkownikow:
            print(i["imie"])
    elif a == "4": # usuwa uzytkownika
        kto = input("Użytkownik: ")
        for i in range(0, len(bazaUzytkownikow)):
            if bazaUzytkownikow[i]["imie"] == kto:
                del bazaUzytkownikow[i]
    elif a == "5": # wyjscie
        break
    else:
        print("Error 404: not found")
    print("\n")
