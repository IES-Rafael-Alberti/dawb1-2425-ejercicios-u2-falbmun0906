# Ejercicio 2.2.25

# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

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

def contar_letras_en_palabra(frase: str):
    frase = ((frase.replace(",", "")).replace(".", "")).split(" ")
    palabra_larga = ""

    for palabra in frase:
        if not palabra.isdigit():
            if len(palabra) > len(palabra_larga):
                palabra_larga = palabra
    
    return palabra_larga

def main():
    frase = pedir_frase()
    print(f"La palabra más larga de las introducidas es: {contar_letras_en_palabra(frase)}")

if __name__ == "__main__":
    main()