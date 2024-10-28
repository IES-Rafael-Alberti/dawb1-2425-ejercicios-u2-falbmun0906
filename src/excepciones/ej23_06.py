# Ejercicio 2.3.5

# Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"

PASSWORD = "password"

def comparar_contrasenia(contrasenia):
    if contrasenia != PASSWORD:
        raise NameError("Incorrect Password!!")

def pedir_contrasenia():
    contrasenia = ""
    try:
        contrasenia = input("Introduce la contraseña: ")
        comparar_contrasenia(contrasenia)
    except NameError as e:
        print(e)
    
    return contrasenia

def main():
    contrasenia = pedir_contrasenia()

    if contrasenia == PASSWORD:
        print("Correct Password!!")

if __name__ == "__main__":
    main()