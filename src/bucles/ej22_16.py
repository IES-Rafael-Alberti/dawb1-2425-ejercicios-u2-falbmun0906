# Ejercicio 2.2.16

# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

def pedir_entero() -> int:
    valor = None
    while valor == None:
        try:
            valor = int(input(f"Introduce un número entero: "))
            if valor < 0:
                print("El número debe ser positivo.")
                valor = None
        except ValueError:
            print("Entrada inválida.")
    
    return valor

def comparar_numero() -> int:
    numero = None
    mayor_numero = 0
    total = 0

    while numero != 0:
        numero = pedir_entero()
        if numero > mayor_numero:
            mayor_numero = numero
    
    return mayor_numero

def main():

    print("El mayor numero introducido es {}.".format(comparar_numero()))

if __name__ == "__main__":
    main()