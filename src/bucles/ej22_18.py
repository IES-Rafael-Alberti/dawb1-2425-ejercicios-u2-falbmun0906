# Ejercicio 2.2.18

# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

def pedir_entero() -> int:
    valor = None
    while valor == None:
        try:
            valor = int(input(f"Introduce un número entero: "))
            if valor < -1:
                print("El número debe ser positivo.")
                valor = None
        except ValueError:
            print("Entrada inválida.")
    
    return valor

def suma_digitos() -> int:
    numero = str(pedir_entero())
    suma = 0

    if numero == "-1":
        return -1, -1
    for digito in numero:
        suma += int(digito)

    return int(numero), int(suma)

def es_par(numero: int) -> bool:

    return numero % 2 == 0

def main():
    numero = 0
    contador_pares = 0

    while numero != -1:
        numero, suma = suma_digitos()
        if numero != -1:
            print("La suma de los dígitos que componen el número {} es {}.".format(numero, suma))
            if es_par(numero):
                contador_pares += 1
    print("Has introducido {} números pares.".format(contador_pares))

if __name__ == "__main__":
    main()