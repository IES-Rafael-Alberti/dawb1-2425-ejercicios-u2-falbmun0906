# Ejercicio 2.3.2

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def comprobar_numero():
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero: "))
            if numero < 0:
                print("El número debe ser positivo.")
                numero = None
        except ValueError:
            print("**ERROR** Entrada inválida.")

    return numero

def pedir_numero():
    numero_correcto = False
    while not numero_correcto:
        numero = comprobar_numero()
        numero_correcto = (numero != None)
    
    return numero

def impares(numero: int):
    serie_impares = ""
    for i in range(1, numero + 1):
        if (i % 2) != 0:
                serie_impares += str(i) + ", "
    serie_impares = serie_impares[:-2]
    
    return serie_impares

def main():
    numero = pedir_numero()
    print(f"Los números impares del 1 al {numero} son: {impares(numero)}.")

if __name__ == "__main__":
    main()