while True:
    salida = input("Introduce un año: ")
    if salida.lower() == 'p':
        break
    try:
        año = int(salida)
        if año < 0:
            raise ValueError
        if año % 4 == 0:
            print("El año es biciesto")
        else:
            print("El año no es biciesto")
    except ValueError:
        print("Error: Se ingreso algo que no es un año")
