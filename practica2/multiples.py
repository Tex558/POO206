try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError):
    print("Error: Valor no válido o división entre cero.")
