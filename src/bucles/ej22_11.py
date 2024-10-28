# Ejercicio 2.2.11

# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
import string

def comprobar_palabra(palabra: str) -> bool:
    if palabra.isalpha():
        return True
    else:
        return False

def dar_vuelta_palabra(palabra: str) -> str:
    palabra_reves = ""
    for letra in palabra:
        palabra_reves = "\n" + letra + palabra_reves
    
    return palabra_reves[1:]

def pedir_palabra() -> str:
    palabra = ""
    palabra_correcta = False

    while not palabra_correcta:
        palabra = input("Introduce una palabra: ")
        if comprobar_palabra(palabra) == True:
            palabra_correcta = True
        else:
            print("La palabra debe estar formada por letras.")

    return palabra

def main():
    palabra = pedir_palabra()

    print(dar_vuelta_palabra(palabra))
        
if __name__ == "__main__":
    main()