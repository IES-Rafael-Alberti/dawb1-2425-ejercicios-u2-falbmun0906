# Ejercicio 2.1.9

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser inferior a cero.")
    if edad > 125:
        raise ValueError("La edad no puede ser superior a 125 años.")

def dame_edad():
    edad = None

    while edad == None:
        try:
            edad = int(input("Introduce tu edad: "))
            validar_edad(edad)
        except ValueError as e:
            if edad == None:
                print("**ERROR** La edad debe ser un número entero.")
            else:
                print("*ERROR** {}".format(e))
                edad = None
    
    return edad

def calcular_precio(edad):
    if edad < 4:
        precio = 0
    elif 4 <= edad < 18:
        precio = 5
    else:
        precio = 10
    
    return precio

def main():
    edad = dame_edad()
    precio = calcular_precio(edad)
    
    print(f"El precio de la entrada es de {precio}€")

if __name__ == "__main__":
    main()