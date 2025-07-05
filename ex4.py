while True:
    numar = input("Introdu un număr: ")
    try:
        check_num = float(numar)
        break
    except ValueError:
        print("Te rog introdu un număr.")

if check_num > 0:
    print("Numărul este pozitiv.")
elif check_num < 0:
    print("Numărul este negativ.")
else:
    print("Numărul este zero.")
