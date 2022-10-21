basket = [[],[]]
while True:
    basket_size = int(input("Cuantos objetos desea agregar?\t"))
    for item in range(basket_size):
        basket[0].append(input("Nombre del articulo:\t"))
        basket[1].append(float(input("Precio del articulo:\t")))
    
    task = int(input("(1) Desea agregar mas articulos\n(2) Terminar\n(3)Imprimir los articulo:\nSeleccione un numero\t"))
    
    match task:
        case 1:
            continue
        case 2:
            break
        case 3:
            sum = 0
            for items in range(len(basket[0])):
                print(f"Articulo: {basket[0][items]} | Precio: {basket[1][items]}")
                sum += basket[1][item]
            print(f"Total:\t|\t{sum}")