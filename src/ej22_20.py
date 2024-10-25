# Ejercicio 2.2.20

# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

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

def coincidencias(letra, frase):
    contador = 0
    coincidencia = ""

    for caracter in frase:
        if caracter != letra:
            print(f"Posición {contador}: No coincide ({caracter})")
            contador += 1
        else:
            coincidencia += f"Posición {contador}: Sí coincide ({caracter})"
            break

    return coincidencia[:-1]

def main():
    frase = pedir_frase()
    letra = pedir_letra()
    
    print(coincidencias(letra, frase))

if __name__ == "__main__":
    main()