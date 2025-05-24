while True:
        def Numeros(frase):
            if frase.isdigit():
                raise ValueError("No se pueden analizar numeros")
            return frase
        
        try: 
            print("Introduce 'a' para cerrar \n")
            frase= input("Ingresa una frase para analizar: ").lower()
            Numeros(frase)
            if frase == "a":
                print("\nFin del programa")
                break
            
            else:
                if frase==frase[::-1] :
                    print("La frase es un palindromo\n")
                else:
                    print("La frase no es un palindromo\n")
                    
        except (ValueError) as Error:
            print("Error :", Error)