while True:
    text = input("Introdu un text: ").strip()
    
    if len(text) < 2 or not any(c.isalpha() for c in text):
        print("Te rog introdu un text valid, cu minim 2 litere.")
    else:
        break

text = text.lower()

frecventa = {}

for litera in text:
    if litera.isalpha():
        frecventa[litera] = frecventa.get(litera, 0) + 1

for litera, numar in frecventa.items():
    print(f"Litera {litera} este in text de : {numar} ori")
