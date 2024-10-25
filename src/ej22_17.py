# Ejercicio 2.2.17

# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

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

def suma_digitos() -> int:
    numero = str(pedir_entero())
    suma = 0

    for digito in numero:
        suma += int(digito)

    return numero, int(suma)

def main():
    numero, suma = suma_digitos()
    print("La suma de los dígitos que componen el número {} es {}.".format(numero, suma))

if __name__ == "__main__":
    main()