# Ejercicio 2.2.7

# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla_multiplicar():
    n = 1
    i = 1
    tabla = f"Tabla del {n}: "
   
    while n < 11:
        if i == 10:
            tabla += str(i * n) + "."
            n += 1
            i = 1
            if n < 11:
                tabla += f"\nTabla del {n}: "
        else:
            tabla += str(i * n) + ", "
            i += 1

    return tabla

def main():
    print(tabla_multiplicar())

if __name__ == "__main__":
    main()