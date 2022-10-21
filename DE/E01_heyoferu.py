menu = ["mostrar", "insertar", "eliminar","salir"]
datos = []

while True: # infinite loop until menu 4, break the while
    for opcion in range(len(menu)):
        print(f"{opcion+1}) {menu[opcion]} ")

    seleccion = int(input("escoger opcion: "))

    match seleccion: # cases for menu

        case 1:
            print(f"Ha seleccionado {menu[seleccion-1]}")
            if len(datos) == 0:
                print(f"Su lista está vacia!")
        
            else:
                for nodo in range(len(datos)):
                    print(f"El N{nodo+1} es {datos[nodo]}.")
        case 2:
            print(f"Ha seleccionado {menu[seleccion-1]}")
            count_limit = int(input(f"Cuantos datos desea agregar?\t"))
            count = 0
            while True:
                datos.append(input(f"Inserte un dato: "))
                count+=1
                if count == count_limit:
                    break

        case 3:
            print(f"Ha seleccionado {menu[seleccion-1]}")
            print(f"¿qué dato quiere eliminar?")
            for nodo in range(len(datos)):
                print(f"{nodo+1}): N{nodo+1} = {datos[nodo]} ")
            datos.pop(int(input("Numero de dato: "))-1)
        
        case 4:
            break
        