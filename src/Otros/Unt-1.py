
MAX_NUMERO = 20

def pedir_entero() -> int:
    valor = None
    while valor == None:
        try:
            valor = int(input(f"Introduce un número entero: "))
            if valor < 0:
                print("El número debe ser positivo.")
                valor = None
            elif valor > MAX_NUMERO:
                print(F"El número tiene que ser menor que {MAX_NUMERO}.")
                valor = None
        except ValueError:
            print("Entrada inválida.")
    
    return valor

def hacer_fila(numero):
    fila = f"{numero} => "
    total = 0

    for i in range(0, numero + 1):
        fila += str(i) + " + "
        total += i
    fila = fila[:-3] + " = " + str(total)
    return fila

def hacer_fila_reves(numero):
    fila = f"{numero} => "
    total = 0

    for i in range(0, numero + 1):
        fila += str(numero - i) + " + "
        total += i
    fila = fila[:-3] + " = " + str(total)
    return fila

def hacer_figura(numero, numero_orig):
    figura = ""

    while numero >= 0:
        if numero == 0:
            figura += "0 => 0\n"
        else:
            figura += hacer_fila(numero) + "\n"
        numero = numero - 1
    
    numero = 1
    while numero != numero_orig + 1:
        figura += hacer_fila_reves(numero) + "\n"
        numero += 1

    return figura[:-1]

def main():
    numero = pedir_entero()
    numero_orig = numero

    print(hacer_figura(numero, numero_orig))

if __name__ == "__main__":
    main()