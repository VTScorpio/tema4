while True:
    nume = input("Introdu numele tau:")
    if nume.isalpha():
        break
    else:
        print("Te rog introdu un nume valid, doar cu litere (fără cifre sau simboluri).")

while True:
    varsta_input = input("Introdu varsta ta (numar întreg): ")
    try:
        varsta = int(varsta_input)
        if varsta > 0:
            break
        else:
            print("Varsta trebuie să fie un numar pozitiv.")
    except ValueError:
        print("Te rog introdu un număr întreg valid pentru vârstă.")

print(f"Bun venit, {nume}! Ai {varsta} ani.")
