# Ejercicio 2.1.3

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

def comprobar_numero(numero):

    salir = False

    while salir != True:
        try:
            numero = float(numero)
            salir = True
        except ValueError:
            print("**ERROR** Número inválido.")
            numero = input("Introduce un número: ")
    return numero

def dame_numeros():

    numero1 = comprobar_numero(input("Introduce el primer número: "))
    numero2 = comprobar_numero(input("Introduce el segundo número: "))

    return numero1, numero2

def division():

    numero1, numero2 = dame_numeros()

    division = numero1 / numero2

    return division

def main():

    print(division())

if __name__ == "__main__":
    main()