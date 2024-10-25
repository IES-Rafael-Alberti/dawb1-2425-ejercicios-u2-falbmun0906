# Ejercicio 2.2.10

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def comprobar_numero(numero):
    if numero < 0:
        raise ValueError("El numero no puede ser inferior a cero.")

def dame_numero():
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un numero entero: "))
            comprobar_numero(numero)
        except ValueError as e:
            if numero is None:
                print("**ERROR** Entrada inválida.")
            else:
                print("**ERROR** {}".format(e))
                numero = None
    
    return numero

def es_primo(numero):
    n_factores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            n_factores += 1
    if n_factores == 2:
        return True
    else:
        return False

def main():
    numero = dame_numero()

    if es_primo(numero):
        print("El número es primo.")
    else:
        print("El numero no es primo.")
        
if __name__ == "__main__":
    main()