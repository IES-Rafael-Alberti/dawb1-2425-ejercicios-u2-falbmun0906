# Ejercicio 2.1.1

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def comprobar_entero(numero):
    try:
        numero = int(numero)
    except ValueError:
        print("**ERROR** Entrada inválida.")
        numero = dame_edad()

    return numero

def dame_edad():
    edad = comprobar_entero(input("Introduce tu edad: "))

    return edad

def es_mayor():
    edad = dame_edad()

    if edad >= 18:
        return "Eres mayor de edad."
    elif edad <= 0:
        return "Aún no has nacido."
    else:
        return "Eres menor de edad."

def main():

    print(es_mayor())

if __name__ == "__main__":
    main()