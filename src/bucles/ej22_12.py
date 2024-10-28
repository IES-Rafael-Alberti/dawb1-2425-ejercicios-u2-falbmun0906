# Ejercicio 2.2.12

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def comprobar_frase(frase: str) -> bool:
    for caracter in frase:
        if not caracter.isalpha() and not caracter.isdigit() and caracter != " " and caracter != "," and caracter != ".":
            return False

    return True

def pedir_frase() -> str:
    frase = ""
    frase_correcta = False

    while not frase_correcta:
        frase = input("Introduce una frase: ")
        if comprobar_frase(frase) == True:
            frase_correcta = True
        else:
            print("La frase debe estar formada por palabras y/o números.")

    return frase

def comprobar_letra(letra: str) -> bool:
    
    return letra.isalpha()

def pedir_letra() -> str:
    letra = ""
    letra_correcta = False

    while not letra_correcta:
        letra = input("Introduce una letra: ")
        if comprobar_letra(letra) == True:
            letra_correcta = True
        else:
            print("**ERROR**")

    return letra

def contar_letras(frase, letra) -> int:
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    
    return contador

def main():
    frase = pedir_frase()
    letra = pedir_letra()
    rep_letra = contar_letras(frase, letra)

    print("La letra '{}' se repite {} veces en '{}'.".format(letra, rep_letra, frase))
        
if __name__ == "__main__":
    main()