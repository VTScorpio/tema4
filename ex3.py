while True:
    numar = input("Introdu un număr: ")
    try:
        check_num = int(numar)
        break  
    except ValueError:
        print("Te rog introdu un număr întreg.")


if check_num % 2 == 0:
    print("Numărul este par.")
else:
    print("Numărul este impar.")
