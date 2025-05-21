try:
    archivo = open("POO.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Fin del intento de lectura.")
