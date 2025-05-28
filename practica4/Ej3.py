while True:
    try:
        frase = input("Introduce una frase: ")
        if frase.strip() == "":
            raise ValueError("La frase esta vacía.")

        letra = input("Introduce una letra: ")
        if len(letra) != 1 or not letra.isalpha():
            raise ValueError("Debe ser una frase con letras.")

        contador = frase.lower().count(letra.lower())
        print(f"La letra '{letra}' aparece {contador} veces en la frase.")

    except ValueError as e:
        print("Error:", e)