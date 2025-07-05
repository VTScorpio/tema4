import random

secret = random.randint(1, 100)

while True:
    incercare = input("Ghicește numărul (1-100): ")

    try:
        check_num = int(incercare)
        if check_num < secret:
            print("Prea mic.")
        elif check_num > secret:
            print("Prea mare.")
        else:
            print("Felicitări! Ai ghicit numărul!")
            break
    except ValueError:
        print("Te rog introdu număr intreg .")
