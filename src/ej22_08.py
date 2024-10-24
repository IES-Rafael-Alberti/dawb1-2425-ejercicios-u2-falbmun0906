# Ejercicio 2.2.8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

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
    serie = ""
    for i in range(1, numero + 1):
        if i % 2 != 0:
            serie += str(i) + " "
            print((serie[::-1]).strip())

def main():
    numero = pedir_entero()
    hacer_triangulo(numero)

if __name__ == "__main__":
    main()