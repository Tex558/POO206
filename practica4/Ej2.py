while True:
    salida = input("Introduce un número: ")
    if salida.lower() == 'p':
        break
    try:
        numero = int(salida)
        if numero < 0:
            raise ValueError
        n = numero
        cuenta_regresiva = []
        while n >= 0:
            cuenta_regresiva.append(n)
            n -= 1
        print("Cuenta regresiva:", ", ".join(map(str, cuenta_regresiva)))
    except ValueError:
        print("Error: Se ingresó un número negativo u otra cosa")
