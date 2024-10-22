# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# Sencillo: El programa muestra el error y finaliza; o muestra los años y finaliza.

# Extra 1:
    # def pedir_edad() -> int
    # def mostrar_anios_cumplidos(edad: int):
# Extra 2_ Lanzar excepciones con mensajes específicos si la edad es negativa, igual a 0 o superior a 125 años.
# Extra 3: Evita mostrar un mensaje en inglés.
# Extra 4: Usar también otra función validar_edad(edad: int)

def validar_edad(edad: int):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad == 0:
        raise ValueError("La edad no puede ser cero.")
    if edad > 125:
        raise ValueError("La edad no puede ser superior a 125.")

def pedir_edad():
    edad = None

    while edad == None:
        try:
            edad = int(input("Introduce tu edad: "))
            validar_edad(edad)     
        except ValueError as e:
            if edad is None:
                print(f"**ERROR** ¡El número introducido no es válido! ¡Inténtalo de nuevo!")
            else:
                edad = None
                print(f"**ERROR** {e}. Inténtalo de nuevo.")

    return edad

def mostrar_anios_cumplidos(edad: int):
    serie = ""

    for i in range(1, edad + 1):
        if i != edad:
            serie += str(i) + ", "
        else:
            serie += str(i) + "."
    print(serie)

def main():
    edad = pedir_edad()
    if edad != None:
        mostrar_anios_cumplidos(edad)

if __name__ == "__main__":
    main()