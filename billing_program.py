items = {
    "chocolate": 50,
    "lays": 20,
    "chewing gum": 30,
    "kurkure": 20,
    "kitkat": 100,
    "oreo": 20,
    "kinder joy": 50,
    "coffee pack": 10,
    "bladelets": 200,
    "ramen": 50,
}
total = 0

while True:
    need = input("What do you need? ").lower()
    if need == "done":
        break

    if need in items:
        print(f"{need}: {items[need]}")
        while True:
            try:
                how_many = int(input("How much do you need? "))
                if how_many > 0:
                    break
                print("Please type a number above 0.")
            except ValueError:
                print("Please type a number, example = 2")
        total = total + items[need] * how_many
        print(f"Running total: {total}rs")
    else:
        print("Sorry! We dont have it")

print(f"Total bill: {total}rs")
