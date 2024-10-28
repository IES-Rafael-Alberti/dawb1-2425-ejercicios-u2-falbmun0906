# Ejercicio 2.2.21

# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def pedir_float() -> float:
    valor = None
    while valor == None:
        try:
            valor = float(input(f"Introduce un monto: "))
            if valor < 0:
                valor = None
        except ValueError:
            print("Entrada inválida.")
    
    return valor

def sumatoria() -> float:
    numero = None
    total = 0
    while numero != 0:
        numero = pedir_float()
        total += numero
    
    if total > 1000:
        total *= 1.1

    return total

def main():
    print("El total a pagar es de {:.2f}€.".format(sumatoria()))

if __name__ == "__main__":
    main()