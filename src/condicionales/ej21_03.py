# Ejercicio 2.1.3

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

def comprobar_numero(valor: str) -> float:
        numero = None
        try:
            numero = float(valor)
        except ValueError:
            print("**ERROR** Número inválido.")

        return numero

def pedir_numero(msj: str) -> float:
    numero_correcto = False
    while numero_correcto == False:
        numero = comprobar_numero(input(msj))
        numero_correcto = (numero != None)

    return numero

def division(numero1, numero2):
    division = None
    try:
        division = numero1 / numero2
    except ZeroDivisionError:
       print("ERROR")

    return division

def main():
    division_chunga = True
    while division_chunga == True:
        numero1 = pedir_numero("Introduce el primer número: ")
        numero2 = pedir_numero("Introduce el segundo número: ")

        try:
            resultado = numero1 / numero2
            print("El resultado de {} entre {} es {}.".format(numero1, numero2, resultado))
            division_chunga = False
        except ZeroDivisionError:
            print("**ERROR** La división entre cero no es posible.")

if __name__ == "__main__":
    main()