# Ejercicio 2.2.5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de anios, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# # Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# # En donde:
# # - amount: Cantidad a invertir
# # - interest: Interes porcentual anual 

def pedir_comprobar_numero(msj_entrada: str, msj_desc_error: str, validar_entero: bool = False) -> float:
    valor = None
    while valor is None:
        try:
            valor = float(input(f"Introduce {msj_entrada}: ").replace(",", "."))
            if valor < 0:
                print(f"{msj_desc_error} debe ser positiva.")
                valor = None
            elif validar_entero and tiene_decimales(valor):
                print(f"{msj_desc_error} debe ser un número entero.")
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
    msj_entrada = "cantidad a invertir"
    msj_desc_error = "La cantidad"
    
    return pedir_comprobar_numero(msj_entrada, msj_desc_error)

def pedir_interes() -> float:
    msj_entrada = "tipo de interés"
    msj_desc_error = "La tasa de interés"
    
    return pedir_comprobar_numero(msj_entrada, msj_desc_error)

def pedir_anios() -> int:
    msj_entrada = "número de años"
    msj_desc_error = "La cantidad de años"
    validar_entero = True

    return int(pedir_comprobar_numero(msj_entrada, msj_desc_error, validar_entero))

    # años_correcto = False
    # msj_1 = "número de años"
    # msj_2 = "La cantidad de años"
    # # while not años_correcto:
    # #     años = comprobar_entero(msj_1, msj_2)
    # #     años_correcto = (años != None)
    
    # return años

def calculo_capital(cantidad: float, interes: float, anios: int) -> float:
    for i in range(anios):
        cantidad = cantidad * (1 + (interes / 100))

    return cantidad

def main():
    cantidad = pedir_cantidad()
    interes = pedir_interes()
    anios = pedir_anios()
    capital = calculo_capital(cantidad, interes, anios)

    print("Con una inversión de {} y un tipo de interés del {}%, tras {} años, el capital asciende a: {:.2f}".format(cantidad, interes, anios, capital))

if __name__ == "__main__":
    main()