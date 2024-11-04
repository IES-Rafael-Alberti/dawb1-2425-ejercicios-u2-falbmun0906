# Ejercicio 2.2.6

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

def pedir_entero() -> int:
    valor = None
    while valor == None:
        try:
            valor = int(input(f"Introduce un número: "))
            if valor < 0:
                print(f"El número debe ser positivo.")
                valor = None
        except ValueError:
            print("Entrada inválida.")
    
    return valor

def hacer_triangulo(numero):
    for i in range(1, numero + 1):
        print("*" * i )

def main():
    numero = pedir_entero()
    hacer_triangulo(numero)

if __name__ == "__main__":
    main()