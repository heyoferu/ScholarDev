## Datos de inmuebles
inmuebles = {
    "A":{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    "B":{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    "C":{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    "D":{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    "E":{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
}
## Precios calculados de cada inmueble
inmuebles_precios = {
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
}


def inmueblesVal(): ## Esta funcion calcula el precio de cada inmueble
    for items in inmuebles:
        antiguedad = 2022 - inmuebles[items]['año']
        if inmuebles[items]['zona'] == 'A':
            precio_a = (inmuebles[items]['metros'] * 1000 + inmuebles[items]['habitaciones'] * 5000 + inmuebles[items]['garaje'] * 15000) * (1 - antiguedad / 100)
            inmuebles_precios[items] = precio_a
        if inmuebles[items]['zona'] == 'B':
            precio_b = (inmuebles[items]['metros'] * 1000 + inmuebles[items]['habitaciones'] * 5000 + inmuebles[items]['garaje'] * 15000) * (1 - antiguedad / 100) * 1.5
            inmuebles_precios[items] = precio_b

menu = ["Listar inmuebles","Calcular presupuesto","Salir"]

while True:
    print("\n"+"Bienes raices".upper().center(100,"*"))
    for i in range(len(menu)): # imprimir opciones disponibles del menu
        print(f"({i+1})\t{menu[i]}")
    
    task = int(input("Seleccione una opcion:\t")) # selecion de menu

    match task: # Verificar si lo que recibe task cumple con algun caso de nuestro menu
        case 1: # listando inmuebles
            for nin in inmuebles:
                print(f"inmueble {nin}".upper().center(100,"="))
                print(f"Año:\t{inmuebles[nin]['año']}")
                print(f"Metros:\t{inmuebles[nin]['metros']}")
                print(f"Habitaciones:\t{inmuebles[nin]['habitaciones']}")
                print(f"Garaje:\t{inmuebles[nin]['garaje']}")
                print(f"Zona:\t{inmuebles[nin]['zona']}")

        case 2:
            ## Precios calculados de cada inmueble dentro de un diccionario
            inmuebles_precios = {"A":0,"B":0,"C":0,"D":0,"E":0}
            inmueblesVal() # Funcion para calcular precios
            presupuesto = float(input("Introducir presupuesto:\t")) # presupuesto
            
            inmuebles_precios['pre'] = int(presupuesto) # asignando el presupuesto a nuestro diccionario de precios

            # ordenando de menor a mayor para imprimir el menor y el mayor proximo a nuestro presupuesto
            inmuebles_reorder = dict(sorted(inmuebles_precios.items(), key=lambda item: item[1])) 

            # indexando nuestros precios reordenados en una lista para identar uno atras y uno adelante +1 y -1
            irindex = list(inmuebles_reorder.values())
            
            # ciclo for para idexar precios
            for i in range(len(irindex)):
                if irindex[i] == presupuesto: # si el dato de la posicion i es igual a nuestro presupuesto
                    minP = False # Asignar variables en caso de no encontrar casas de menor o mayor precio
                    maxP = False # """"

                    print("\nInmueble con precio menor al presupuesto".upper())

                    for nin in inmuebles_reorder: # ciclo for de nuestros reordenado de inmuebles
                        # si la clave nin es igual al anterior (-1) de nuestra lista de precios
                        # y evitamos que haga reversa si es menor a nuestro presupuesto
                        # entonces nos imprime el precio y el nombre del inmueble dentro de esa clave
                        if inmuebles_reorder[nin] == irindex[i-1] and inmuebles_reorder[nin] < presupuesto:
                            print(f"Inmueble: {nin}\t|\tPrecio: {irindex[i-1]}")
                            minP = True # retorna verdadero si se ha encontrado

                    if minP == False: # si no se encontro un menor precio entonces se mantiene como falso e imprime lo siguiente
                        print("No hay inmuebles de menor precio!")

                    print(f"\nPresupuesto:\t{presupuesto}\n")

                    print("Inmueble con precio mayor al presupuesto".upper())

                    for nin in inmuebles_reorder: # ciclo for de nuestros reordenado de inmuebles
                        try: # usamos try para valuar errrores
                            # Si la clave nin es igual al siguiente (+1) de nuestra lista de precios
                            # entonces nos imprime el precio y el nombre del inmueble dentro de esa clave
                            if inmuebles_reorder[nin] == irindex[i+1]:
                                print(f"Inmueble: {nin}\t|\tPrecio: {irindex[i+1]}")
                                maxP = True # Retorna true si se ha encontrado
                        except IndexError: #Si tuvieras un error de index porque nuestro presupuesto es mayor maxP sigue siendo falso
                            maxP = maxP
                    if maxP == False: # Si es falso no hay precios mayores al presupuesto
                        print("No hay inmuebles de mayor precio!")
            

            # ciclos para listar todos los precios ordenados en relacion al presupuesto
            print("\n"+"Listando todos los precios disponibles en relacion a su presupuesto...")
            for nin in inmuebles_reorder:
                if inmuebles_reorder[nin] < presupuesto:
                    print(f"Inmueble:{nin}\t|\tPrecio: {inmuebles_reorder[nin]}".upper())
            
            print(f"Presupuesto:\t|\tMonto: {presupuesto}".upper())

            for nin in inmuebles_reorder:
                if inmuebles_reorder[nin] > presupuesto:
                    print(f"Inmueble:{nin}\t|\tPrecio: {inmuebles_reorder[nin]}".upper())


        case 3: # Caso 3 para salir
            break