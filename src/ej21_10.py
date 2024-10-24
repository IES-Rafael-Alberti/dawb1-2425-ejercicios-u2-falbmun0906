# Ejercicio 2.1.10

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

def tipo_pizza() -> bool:
    tipo = False
    tipo_correcto = False
    # Validación de 'tipo'
    while tipo_correcto == False:
        tipo = input("¿Quieres una pizza vegetariana? Sí/No: ").lower()
        if tipo == "s" or tipo == "sí" or tipo == "si":
                tipo_correcto = True
                tipo = True
        elif tipo == "n" or tipo == "no":
                tipo_correcto = True
                tipo = False
        else:
            print("**ERROR** Responda con Sí/No")
    if tipo:
         print("Ha elegido una pizza vegetariana, ¿cuál de los siguientes ingredientes quieres añadir?\n1.- Pimiento\n2.- Tofu")
    else:
        print("Ha elegido una pizza no vegetariana, ¿cuál de los siguientes ingredientes quieres añadir?\n1.- Peperoni\n2.- Jamón\n3.- Salmón")
    
    return tipo

def introduce_ingrediente(tipo: bool) -> str:
    ingrediente_correcto = False
    while ingrediente_correcto == False:
        if tipo: # Si 'tipo' es True, el cliente ha pedido una pizza vegetariana.
            ingrediente = input("Introduce un ingrediente: ").lower()
            if comprobar_ingrediente(ingrediente, tipo):
                 ingrediente_correcto = True             
        else:
            ingrediente = input("Introduce un ingrediente: ").lower()
            if comprobar_ingrediente(ingrediente, tipo):
                ingrediente_correcto = True

    # Reasigno los valores de ingredientes si han optado por meter el código del ingrediente.
    if tipo == True: # Si es vegetariana.
        if ingrediente == "1": ingrediente = "Pimiento"
        elif ingrediente == "2": ingrediente = "Tofu"
    if tipo == False: # Si no es vegetariana.
        if ingrediente == "1": ingrediente = "Peperoni"
        elif ingrediente == "2" or ingrediente == "jamon": ingrediente = "Jamón"
        elif ingrediente == "3" or ingrediente == "salmon": ingrediente = "Salmón"
    
    return ingrediente # Devuelvo el ingrediente, con la primera letra en mayúscula y con tilde (si la tuviese).

def comprobar_ingrediente(ingrediente: str, tipo: bool):
    ingrediente = ingrediente.lower()
    
    if tipo == True:
        if ingrediente == "1" or ingrediente == "2" or ingrediente == "pimiento" or ingrediente == "tofu":
            return True
        else:
            print("\n**ERROR** Introduce el nombre o el código del ingrediente.")
            return False
    elif tipo == False:
        if ingrediente == "1" or ingrediente == "2" or ingrediente == "3" or ingrediente == "peperoni" or ingrediente == "jamón" or ingrediente == "jamon" or ingrediente =="salmón" or ingrediente == "salmon":
            return True
        else:
            print("\n**ERROR** Introduce el nombre o el código del ingrediente.")
            return False

def main():
    tipo = tipo_pizza()
    ingrediente = introduce_ingrediente(tipo)

    if tipo:
        print("Has elegido una pizza vegetariana con: tomate, mozarella y {}.".format(ingrediente.lower()))
    if not tipo:
        print("Has elegido una pizza no vegetariana con: tomate, mozarella y {}.".format(ingrediente.lower()))

if __name__ == "__main__":
    main()