# Ejercicio 2.2.24

# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def pedir_entero() -> int:
    valor = None
    while valor == None:
        try:
            valor = int(input(f"Introduce un número entero: "))
            if valor <= 1 and valor != 0:
                print("El número debe ser mayor que uno.")
                valor = None
        except ValueError:
            print("Entrada inválida.")
    
    return valor

def es_primo(numero: int) -> bool:
    contador_factores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador_factores += 1

    if contador_factores == 2:
        return True
    else:
        return False

def contar_primos() -> int:
    numero = None
    contador_primos = 0
    while numero != 0:
        numero = pedir_entero()
        if es_primo(numero):
            contador_primos += 1
    
    return contador_primos

def main():
    print("Se han introducido {} número/s primo/s.".format(contar_primos()))

if __name__ == "__main__":
    main()