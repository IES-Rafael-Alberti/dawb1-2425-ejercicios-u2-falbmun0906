# Ejercicio 2.1.5

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def comprobar_float(numero):
    try:
        numero = float(numero)
    except ValueError:
        print("**ERROR** Entrada inválida.")
        numero = None        

    return numero

def dame_ingresos():
    ingresos = None
    while ingresos is None:
        ingresos = comprobar_float(input("Introduce tus ingresos: "))

    return ingresos

def comprobar_entero(valor: str):
    try:
        numero = int(valor)
    except ValueError:
        print("**ERROR** Entrada inválida.")
        numero = None    

    return numero

def dame_edad():
    edad = None
    while edad is None:
        edad = comprobar_entero(input("Introduce tu edad: "))

    return edad

def es_elegible(edad, ingresos):
    if edad >= 16 and ingresos >= 1000:
        return True
    else:
        return False

def main():
    edad = dame_edad()
    ingresos = dame_ingresos()
    elegible = es_elegible(edad, ingresos)

    if elegible:
        print("Tienes {} años y tus ingresos son de {:.2f}. Debes tributar.".format(edad, ingresos))
    else:
        print("Tienes {} años y tus ingresos son de {:.2f}. NO debes tributar.".format(edad, ingresos))
    
if __name__ == "__main__":
    main()