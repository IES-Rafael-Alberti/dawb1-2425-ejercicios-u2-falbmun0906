# Ejercicio 2.2.9

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def pedir_clave():
    clave_usuario = input("Introduce tu contraseña: ")

    return clave_usuario

def comprobar_contrasenia():
    clave = "contraseña"
    clave_usuario = pedir_clave()
    salir = False

    while salir != True:
        if clave_usuario.lower() == clave:
            salir = True
        else:
            print("Contraseña incorrecta.")
            clave_usuario = pedir_clave()

    return True

def main():
    if comprobar_contrasenia():
        print("Contraseña correcta.")
        
if __name__ == "__main__":
    main()