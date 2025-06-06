"Programa que pide al ususario dos palabras y que dice cual es mas larga"
while True:
    p1 = input("Ingrese un texto: ")
    p2 = input("Ingrese un segundo texto: ")

    if p1.lower() == 'p':
        break    
    try:
        if p1.isdigit():
            raise ValueError
        if p2.isdigit():
            raise ValueError
        
        if len (p1) > len(p2):
            print(f"El texto '{p1}' es más larga que '{p2}' por {len(p1) - len(p2)} caracteres.")
        else: 
            print(f"El texto '{p2}' es más larga que '{p1}' por {len(p2) - len(p1)} caracteres.")
            
    except ValueError:
        print("no se ingreso una palabra o una de las palabras consta de numeros")
