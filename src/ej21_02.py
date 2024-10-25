# Ejercicio 2.1.2

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def pedir_clave():
    clave_usuario = input("Introduce tu contraseña: ")

    return clave_usuario

def comprobar_contrasenia():
    clave = "contraseña"
    clave_usuario = pedir_clave()
    salir = False

    while salir != True:
        if clave_usuario.lower() == clave:
            return True
        else:
           return False

def main():
    if comprobar_contrasenia():
        print("La contraseña es correcta.")
    else:
        print("La contraseña es incorrecta.")
        
if __name__ == "__main__":
    main()