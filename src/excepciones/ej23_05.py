# Ejercicio 2.3.4

# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def pedir_numero():
    numero = None
    try:
        numero = int(input("Introduce un número entero: "))
    except ValueError as e:
        print("**ERROR** Entrada inválida.")
        raise e
    
    return numero

def main():
    numero = pedir_numero()

if __name__ == "__main__":
    main()