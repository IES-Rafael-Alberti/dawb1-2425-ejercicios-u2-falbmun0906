# Ejercicio 2.2.1

# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repetir_palabra(palabra):
    repeticion = ""
    for i in range (10):
        repeticion += palabra + "\n"
    
    return repeticion[:-1]

def main():
    palabra = input("Introduce una palabra: ")
    print(repetir_palabra(palabra))

if __name__ == "__main__":
    main()