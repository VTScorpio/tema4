def patrat(numar):
    return numar ** 2

while True:
    numar = input("Introdu un număr: ")
    try:
        check_num = float(numar)
        break
    except ValueError:
        print("Te rog introdu un număr.")

print(f"Patratul numarului  {check_num} este {patrat(check_num)}" )
