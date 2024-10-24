# Ejercicio 2.2.2

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def comprobar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser inferior a cero.")
    elif edad == 0:
        raise ValueError("La edad no puede ser igual a cero.")
    elif edad >= 125:
        raise ValueError("La edad no puede ser superior a 125.")

def pedir_edad() -> int:
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

def serie_edad(edad):
    for i in range(1, edad + 1):
        print(i)
    
    # En una línea separado por comas.
    
    # serie = ""
    # for i in range(1, edad + 1):
    #     if i < edad:
    #         serie += str(i) + ", "
    #     else:
    #         serie += str(i) + "."

    # return serie

def main():
    edad = pedir_edad()
    serie_edad(edad)
    
    # serie = serie_edad(edad)
    # print(f"A lo largo de tu vida has cumplido: {serie}")

if __name__ == "__main__":
    main()