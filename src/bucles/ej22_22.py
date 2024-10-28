# Ejercicio 2.2.22

# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

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

def contar_par_impar() -> int:
    numero = str(pedir_entero())
    contador_pares = 0
    contador_impares = 0

    for digito in numero:
        if int(digito) % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1

    return int(numero), contador_pares, contador_impares

def main():
    numero = None
    total_pares = 0
    total_impares = 0

    while numero != 0:
        numero, pares, impares = contar_par_impar()
        if numero == 0:
            print("Se han introducido un total de {} dígito/s par y {} dígito/s impar.".format(total_pares, total_impares))
        else:
            print("Entre los dígitos que componen {} hay {} par y {} impar.".format(numero, pares, impares))
            total_pares += pares
            total_impares += impares

if __name__ == "__main__":
    main()