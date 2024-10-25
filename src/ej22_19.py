# Ejercicio 2.2.19

# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

def pedir_opcion():
    opcion = None
    while opcion == None:
        opcion = input("-> ")
        if opcion != "1" and opcion != "2" and opcion != "3":
            print("Introduzca una opción válida (1, 2 ó 3).")
            opcion = None

    return opcion

def main():
    opcion = None
    while opcion != "3":
        print("1- Comenzar programa.\n2- Imprimir listado.\n3- Finalizar programa.\n")
        opcion = pedir_opcion()
        if opcion == "1":
            print("\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Ut id ornare tortor, quis eleifend leo. Etiam euismod iaculis nisi. Integer feugiat accumsan ante, eget congue nibh convallis eget. Maecenas odio augue, ullamcorper lobortis suscipit vitae, aliquam sed dui. Nulla sed ligula a sapien porta lobortis. Vestibulum ut varius arcu, at feugiat ipsum. Integer lacinia tincidunt tempus. Nullam sit amet aliquet risus. Nulla hendrerit augue in leo sollicitudin fermentum. Etiam id mi sed orci porta euismod ut eget elit. Quisque eget nisi ullamcorper, feugiat sapien nec, rhoncus nunc. Suspendisse bibendum lectus sed suscipit bibendum. Vestibulum id lacinia felis. Pellentesque ut vestibulum orci.\n")
        elif opcion == "2":
            print("\nNunc fermentum risus eget iaculis dapibus. Morbi sodales, odio in mollis efficitur, neque augue molestie tortor, eleifend vestibulum tortor tellus at purus. Sed congue quis felis a pharetra. Proin sagittis eget ligula vitae vestibulum. Donec dignissim odio id nibh imperdiet elementum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc mattis convallis dolor venenatis consequat. Nullam sed ipsum ut metus congue ultrices laoreet ac nunc. Donec dictum tincidunt neque id posuere. Aenean ultrices metus et erat dapibus malesuada. In sit amet congue dui. Nulla eget consequat risus. Morbi rhoncus pharetra elit, eget malesuada libero consequat ac. Nam vulputate nec est ac hendrerit.\n")

if __name__ == "__main__":
    main()