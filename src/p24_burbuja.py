# Algoritmo burbuja (ordenar array).

def comprobar_entero(numero: str) -> bool:
    """
    Verifica si el argumento proporcionado puede ser convertido a un entero.

    Args:
        numero (str): El valor a verificar.

    Returns:
        bool: True si el valor es un número entero, False en caso contrario.
    """

    try:
        numero = int(numero)
    except ValueError:
        print("**ERROR** El número debe ser entero.")
        return False
    
    return True

def pedir_numero() -> int:
    """
    Solicita al usuario un número entero y lo valida.

    Returns:
        int: El número entero ingresado por el usuario.
    """

    numero_correcto = False
    while not numero_correcto:
        numero = input("Introduce número: ")
        if comprobar_entero(numero):
            numero_correcto = True
    
    return int(numero)

def pedir_lista() -> list:
    """
    Solicita al usuario una lista de números enteros.

    El usuario puede introducir números hasta que introduzca 0, 
    que indica el final de la entrada.

    Returns:
        list: Una lista de números enteros ingresados por el usuario.
    """

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
    """
    Ordena una lista de números enteros solicitada al usuario.

    Returns:
        list: La lista de números enteros ordenada de menor a mayor.
    """
    
    lista = pedir_lista()
    longitud = len(lista)

    for i in range(0, longitud):
        for j in range(0, (longitud - 1) - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def main():
    """
    Muestra la lista ordenada de números enteros ingresados por el usuario.
    """

    print(ordenar_lista())

if __name__ == "__main__":
    main()