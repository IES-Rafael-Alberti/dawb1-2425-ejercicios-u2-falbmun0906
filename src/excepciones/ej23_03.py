# Ejercicio 2.2.4

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def comprobar_numero():
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero: "))
            if numero <= 0:
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

def cuenta_atras(numero):
    serie = ""
    for i in range(numero, -1, -1):
        serie += str(i) + ", "
    serie = serie[:-2] # Quito ", " de la última iteración.

    return serie

def main():
    numero = pedir_numero()
    if numero != None:
        print(f"{cuenta_atras(numero)}.")

if __name__ == "__main__":
    main()