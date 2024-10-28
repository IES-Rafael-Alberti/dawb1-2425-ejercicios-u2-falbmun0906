# Ejercicio 2.2.13

# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def main():
    salir = False

    while not salir:
        cadena = input("Introduce algo: ")
        if cadena.lower() == "salir":
            salir = True
        else:
            print(cadena)
        
    print("Fin del programa")

if __name__ == "__main__":
    main()