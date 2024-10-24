# Ejercicio 2.1.6

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

import string

def introducir_nombre(abc: str) -> str:
    nombre = input("Introduce tu nombre: ")
    nombre_correcto = False
    while not nombre_correcto:
        for letra in abc:
            if nombre.lower().startswith(letra):
                nombre_correcto = True
        if nombre_correcto == False:
            print("**ERROR** Nombre inválido.")
            nombre = input("Introduce tu nombre: ")

    return nombre

def introducir_sexo() -> bool:
    sexo = input("Introduce tu sexo: ")
    sexo_correcto = False

    while not sexo_correcto:
        if sexo.lower() == "hombre" or sexo.lower() == "h":
            sexo = True
            sexo_correcto = True
        elif sexo.lower() == "mujer" or sexo.lower() == "m":
            sexo = False
            sexo_correcto = True
        else:
            print("**ERROR** de formato. Entradas válidas: [Hombre/Mujer], [hombre/mujer], [H/M], [h/m].")
            sexo = input("Introduce tu sexo: ")

    # True = H; False = M

    return sexo

def letra_nombre(nombre: str, abc) -> bool:
    for letra in abc[0:14]:
        if nombre.startswith(letra):
            return True
 
    return False

def crear_abc() -> list:
    # Explicación de Diiego (mucho más fácil)
    # abecedario = string.ascii_lowercase
    # pos_n = abecedario.find("n")
    # abecedario = abecedario[:pos_n + 1] + "ñ" + abecedario[pos_n + 1:]
    abecedario = []
    ult_letra = ""
    
    for letra in string.ascii_lowercase:
        if ult_letra == "n":
            abecedario.append("ñ")
        abecedario.append(letra)
        ult_letra = letra

    return abecedario

def elegir_clase(letra_inicial, sexo) -> bool:
    if not sexo and letra_inicial or sexo and not letra_inicial:
        return True
    else:
        return False

def main():
    abc = crear_abc()
    nombre = introducir_nombre(abc).lower()
    sexo = introducir_sexo() #True = H / False = M
    letra_inicial = letra_nombre(nombre, abc) #True = A-M / False = Ñ-Z

    if elegir_clase(letra_inicial, sexo):
        print("Hola, {}. Tu grupo es el A.".format(nombre.title()))
    else:
        print("Hola, {}. Tu grupo es el B.".format(nombre.title()))

if __name__ == "__main__":
    main()