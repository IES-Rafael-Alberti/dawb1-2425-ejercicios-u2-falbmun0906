# Ejercicio 2.2.2

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def comprobar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser inferior a cero.")
    elif edad == 0:
        raise ValueError("La edad no puede ser igual a cero.")
    elif edad >= 125:
        raise ValueError("La edad no puede ser superior a 125.")

def pedir_edad():
    edad = None
    while edad == None:
        try:
            edad = int(input("Introduce tu edad: "))
            comprobar_edad(edad)
        except ValueError as e:
            if edad == None:
                print("**ERROR** Introduce un edad válida.")
            else:
                print(f"**ERROR** {e}")
                edad = None
    
    return edad

def main():
    edad = pedir_edad()

    print(edad)

if __name__ == "__main__":
    main()