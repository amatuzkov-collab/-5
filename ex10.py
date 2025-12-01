pin = input()

if len(pin) == 4 and pin.isdigit() and len(set(pin)) == 4:
    year = int(pin)
    if 1900 <= year <= 2050:
        print("ERROR")
    else:
        print("OK")
else:
    print("ERROR")
