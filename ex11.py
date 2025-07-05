def maxim (a, b):
    return a if a > b else b

while True:
    numar1 = input("Introdu primul număr: ")
    try:
        check_num1 = float(numar1)
        break
    except ValueError:
        print("Te rog introdu primul număr.")


while True:
    numar2 = input("Introdu al doilea număr: ")
    try:
        check_num2 = float(numar2)
        break
    except ValueError:
        print("Te rog introdu al doilea număr.")        


print (f"Cel mai mare numar dintre {check_num1} si {check_num2} este {maxim(check_num1,check_num2)} ")
