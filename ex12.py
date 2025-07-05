def palindrom(cuvant):
    return cuvant == cuvant[::-1]

while True:
    cuv = input("Introdu un cuvant:")
    if cuv.isalpha():
        break
    else:
        print("Te rog introdu un cuvant, doar cu litere (fără cifre sau simboluri).")

if palindrom(cuv) == True:
    print (f"Cuvantul introdus {cuv} este palindrom ")
else:
    print (f"Cuvantul introdus {cuv} nu este palindrom ")
