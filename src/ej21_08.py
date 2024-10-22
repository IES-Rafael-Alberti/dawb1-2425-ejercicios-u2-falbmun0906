# Ejercicio 2.1.8

# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	    0.4
# Meritorio	    0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

def validar_puntuacion(puntuacion):
    if puntuacion < 0:
        raise ValueError("La puntuación no puede ser inferior a cero.")
    elif puntuacion > 1:
        raise ValueError("La puntuación no puede ser superior a uno.")

def introduce_puntuacion():
    puntuacion = None
    while puntuacion == None:
        try:
            puntuacion = float(input("Introduce su puntuación: "))
            validar_puntuacion(puntuacion)
        except ValueError as e:
            if puntuacion == None:
                print("**ERROR** Entrada inválida.")
            else:
                puntuacion = None
                print("**ERROR** {}".format(e))

    return puntuacion

def niveles_rend(puntuacion):
    if 0 <= puntuacion < 0.4:
        rendimiento = 0
    elif 0.4 <= puntuacion < 0.6:
        rendimiento = 0.4
    elif 0.6 <= puntuacion:
        rendimiento = 0.6

    return rendimiento

def main():
    puntuacion = introduce_puntuacion()
    rendimiento = niveles_rend(puntuacion)
    bonus = rendimiento * 2400

    print("Tu puntuación es de {}, por lo que te corresponden {}€".format(puntuacion, bonus))

if __name__ == "__main__":
    main()