# Ejercicio 2.2.7

# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla_multiplicar():
    n = 1
    i = 1

    print(f"Tabla del {n}:")
    while n < 11:
        print(i * n)
        if i == 10:
            n += 1
            i = 1
            if n < 11:
                print(f"Tabla del {n}:")
        else:
            i += 1

def main():
    tabla_multiplicar()

if __name__ == "__main__":
    main()