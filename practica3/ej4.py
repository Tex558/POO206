while True:
    try: 
        print("Introduce 'p' para finalizar\n")
        contraseña= input("Introduce una contraseña: ")
        especiales = "!@#$%^&*()-_=+{}[]:;\"'<>.,?/\\|`~"

        cEspecial = False
        for char in contraseña:
            if char in especiales:
                cEspecial = True
                break
        
        if contraseña == 'p':
            print("\nFin del programa")
            break
        
        else:
            if not contraseña.strip():
                print("La contraseña no puede estar vacia")
            elif " " in contraseña:
                print("La contraseña no puede tener espacios")
            elif len(contraseña)<=10:
                print("La contraseña es demasiado corta")
            elif not any(char.isdigit() for char in contraseña):
                print("La contraseña debe contener un numero")
            elif not cEspecial:
                print ("La contraseña debe contener un caracter especial")
            else:
                print("\nLa contraseña es valida\n")
                
    except Exception as Error: 
        print("Error: ", Error)