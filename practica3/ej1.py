while True:
    salida = input("Introduce un numero: ")
    if salida.lower() == 'p':
        break
    try:
        numero = int(salida)
        if numero < 0:
            raise ValueError
        if numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero no es par")
    except ValueError:
        print("Error: Se ingreso algo que no es un numero entero")
