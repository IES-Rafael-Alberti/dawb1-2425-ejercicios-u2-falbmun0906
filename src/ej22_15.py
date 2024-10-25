# Ejercicio 2.2.15

# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

def pedir_entero() -> int:
    valor = None
    while valor == None:
        try:
            valor = int(input(f"Introduce un número entero: "))
            if valor < 0:
                valor = None
        except ValueError:
            print("Entrada inválida.")
    
    return valor

def sumatoria() -> int:
    numero = None
    total = 0
    while numero != 0:
        numero = pedir_entero()
        total += numero
    
    return total

def main():

    print("La sumatoria de los números positivos introducidos es {}.".format(sumatoria()))

if __name__ == "__main__":
    main()