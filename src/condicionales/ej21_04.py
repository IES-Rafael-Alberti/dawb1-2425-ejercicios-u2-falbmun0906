# Ejercicio 2.1.4

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def comprobar_entero(numero):
    try:
        numero = int(numero)
    except ValueError:
        print("**ERROR** Entrada inválida.")
        numero = None        

    return numero

def dame_numero():
    numero = None
    while numero is None:
        numero = comprobar_entero(input("Introduce un número entero: "))
    
    return numero
    
def es_par():
    numero = dame_numero()

    if numero % 2 == 0:
        return numero, True
    else:
        return numero, False

def main():
    numero, par = es_par()

    if par:
        print("El número {} es par.".format((numero)))
    else:
        print("El número {} es impar.".format((numero)))

if __name__ == "__main__":
    main()