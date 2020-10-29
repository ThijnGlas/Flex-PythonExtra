verzekering_per_maand = € 23
benzine_kosten_per_liter = € 1.54
liter_per_kilometer = 0.2L

while not isinstance(invoer, float);

    try:
        invoer = input("voer een getal in: ")

        invoer = float(invoer)

        print("ja, de invoer " + str(invoer) + " is een getal, want ik kan het omzetten naar een float."

    except ValueError:
        print(invoer + " is geen geldig getal")
