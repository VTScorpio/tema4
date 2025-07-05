numere = []

for i in range(5):
    while True:
        valoare = input(f"Introdu numărul {i+1}: ")
        try:
            numar = float(valoare)
            numere.append(numar)
            break  
        except ValueError:
            print("Te rog introdu un numar valid.")

suma = sum(numere)
media = suma / len(numere)

print(f"Suma: {suma}")
print(f"Media: {media}")
