# Ejercicio 2.2.5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# # Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# # En donde:
# # - amount: Cantidad a invertir
# # - interest: Interes porcentual anual 

def pedir_comprobar_numero(entero: bool, msj_1: str, msj_2: str) -> float:
    valor = None
    while valor is None:
        try:
            valor = float(input(f"Introduce {msj_1}: ").replace(",", "."))
            if valor < 0:
                print(f"{msj_2} debe ser positiva.")
                valor = None
            elif entero and tiene_decimales(valor):
                print(f"{msj_2} debe ser un número entero.")
                valor = None
        except ValueError:
            print("Entrada inválida.")

    return valor

def tiene_decimales(numero: float) -> bool:
    if numero % 1 != 0:
        return True
    else:
        return False

def pedir_cantidad() -> float:
    msj_1 = "cantidad a invertir"
    msj_2 = "La cantidad"
    entero = False
    
    return comprobar_valor(entero, msj_1, msj_2)

def pedir_interes() -> float:
    msj_1 = "tipo de interés"
    msj_2 = "La tasa de interés"
    entero = False
    
    return comprobar_valor(entero, msj_1, msj_2)

def pedir_años() -> int:
    msj_1 = "número de años"
    msj_2 = "La cantidad de años"
    entero = True

    return int(comprobar_valor(entero, msj_1, msj_2))

    # años_correcto = False
    # msj_1 = "número de años"
    # msj_2 = "La cantidad de años"
    # # while not años_correcto:
    # #     años = comprobar_entero(msj_1, msj_2)
    # #     años_correcto = (años != None)
    
    # return años

def calculo_capital(cantidad: float, interes: float, años: int) -> float:
    for i in range(años):
        cantidad = cantidad * (1 + (interes / 100))

    return cantidad

def main():
    cantidad = pedir_cantidad()
    interes = pedir_interes()
    años = pedir_años()
    capital = calculo_capital(cantidad, interes, años)

    print("Con una inversión de {} y un tipo de interés del {}%, tras {} años, el capital asciende a: {:.2f}".format(cantidad, interes, años, capital))

if __name__ == "__main__":
    main()