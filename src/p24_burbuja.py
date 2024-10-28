# Algoritmo burbuja (ordenar array).

def comprobar_entero(numero: str) -> bool:
    try:
        numero = int(numero)
    except ValueError:
        print("**ERROR** El número debe ser entero.")
        return False
    
    return True

def pedir_numero() -> int:
    numero_correcto = False
    while not numero_correcto:
        numero = input("Introduce número: ")
        if comprobar_entero(numero):
            numero_correcto = True
    
    return int(numero)

def pedir_lista() -> list:
    fin = False
    lista = []
    print("Introduce los números que componen la lista. Introduce 0 para finalizar.")
    while not fin:
        numero = pedir_numero()
        if numero == 0:
            fin = True
        else:
            lista.append(numero)
    
    return lista

def ordenar_lista() -> list:
    lista = pedir_lista()
    longitud = len(lista)

    for i in range(0, longitud):
        for j in range(0, (longitud - 1) - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def main():

    print(ordenar_lista())

if __name__ == "__main__":
    main()