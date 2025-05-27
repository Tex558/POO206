while True:
    listaI = []
    salida = input("Introduce un número mayor a 10: ")
    if salida.lower() == 'p':
        break
    try:
        numero = int(salida)
        if numero < 11:
            raise ValueError
        n = 3
        while n < numero:
            if n % 2 != 0:
                listaI.append(n)
            n += 1
        print("Números impares antes de", numero, ":", ", ".join(map(str, listaI)))
    except ValueError:
        print("Error: Se ingresó un número menor a 10 u otra cosa")
