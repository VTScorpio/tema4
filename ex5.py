while True:
    numar = input("Introdu un număr întreg: ")
    try:
        check_num = int(numar)
        break  
    except ValueError:
        print("Te rog introdu un număr întreg.")

for i in range(1, 11):
    print(f"{check_num} x {i} = {check_num * i}")
