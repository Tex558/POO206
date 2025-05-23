while True:
    try:
        año = int(input("Introduce un año: "))

        if año % 4 == 0:
            print("El año es biciesto")
        else:
            print("El año no es biciesto")

    except ValueError:
        print("Error: Se ingreso algo que no es un año")
        break