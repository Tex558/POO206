while True:
    try:
        numero = int(input("Introduce un numero: "))

        if numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero no es par")

    except ValueError:
        print("Error: Se ingreso algo que no es un numero entero")
        break