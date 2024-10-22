# Ejercicio 2.1.7

# # Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	                    Tipo impositivo
# Menos de 10000€	        5%
# Entre 10000€ y 20000€	    15%
# Entre 20000€ y 35000€	    20%
# Entre 35000€ y 60000€	    30%
# Más de 60000€	            45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def introduce_renta():
    renta = None

    while renta == None:
        try:
            renta = float(input("Introduce tu renta anual: "))
            if renta < 0:
                print("La renta no puede ser inferior a cero.")
                renta = None
        except ValueError:
            print(f"**ERROR** ¡El número introducido no es válido! ¡Inténtalo de nuevo!")

    return renta

def comprobar_tipo():
    renta = introduce_renta()

    if renta == 0:
        tipo = 0
    elif renta < 10000:
        tipo = 0.05
    elif 10000 <= renta < 20000:
        tipo = 0.15
    elif 20000 <= renta < 35000:
        tipo = 0.20
    elif 35000 <= renta < 60000:
        tipo = 0.30
    else:
        tipo = 0.45

    return tipo

def main():
    tipo = comprobar_tipo() * 100

    if tipo == 0:
        print("No has tenido ingresos este año.")
    else: 
        print("Te corresponde un tipo impositivo del {:.2f}%".format(tipo))

if __name__ == "__main__":
    main()