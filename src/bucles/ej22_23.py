# Ejercicio 2.2.23

# Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

# Ejemplo de ejecución:
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.

def contar_linea() -> int:
    linea = crear_linea()
    contador_digitos = 0

    if linea == "fin":
        return -1
    else:
        for caracter in linea:
            if caracter.isdigit():
                contador_digitos += 1

    return contador_digitos

def crear_linea() -> str:
    linea = ""
    entrada = ""
    while entrada != "/" and entrada != "*":
        entrada = input("Libro: ")
        linea += entrada
        if entrada == "/":
            return linea
        elif entrada == "*":
            return "fin"

def main():

    contador_dig = None
    contador_lin = 0
    while contador_dig != -1:
        contador_dig = contar_linea()
        if contador_dig == -1:
            print("Fin. Se leyeron {} líneas completas".format(contador_lin))
        else:
            print("Línea completa. Aparecen {} dígitos numéricos.".format(contador_dig))
            contador_lin += 1

if __name__ == "__main__":
    main()