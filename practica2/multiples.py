try:
    numero = int(input("Introduce un numero: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError):
    print("Error: Valor no valido o division entre cero.")
