import random

def randomID():
    cid_size = 10
    print("\nGenerando client id...")
    numeric="0123456789"
    alpha="abcdefghijklmnopqrstuvwxyz"

    temp = numeric + alpha


    clientID = "".join(random.sample(temp,cid_size)).upper()
    return clientID

menu = ["Añadir cliente","Eliminar cliente","Mostrar cliente","Listar todos los clientes","Listar clientes preferentes","Terminar"]
clients_db = {

}
while True:
    for nmenu in range(6):
        print(f"{nmenu+1}) {menu[nmenu]}")
    selection = int(input("Seleccione una opcion:\t"))

    match selection:
        case 1:
            print("Agregar cliente(s)".center(100,"="))
            nc_size = int(input("Numero de clientes a agregar:\t")) 
            for nclients in range(nc_size):
                
                cid = randomID()
                clients_db[cid] = {}
                clients_db[cid]["name"] =  input("Nombre del cliente:\t")
                clients_db[cid]["address"] = input("Direccion del cliente:\t")
                clients_db[cid]["phone"] = input("Telefono:\t")
                clients_db[cid]["mail"] = input("Correo:\t")
            
                typeofclient = input("Tipo de cliente: VIP(V) o cualquier tecla para omitir:\t")
                if typeofclient == "V" or typeofclient == "v":
                    status = True
                else:
                    status = False 
                
                clients_db[cid]["status"] = status

                clients_db.update()
        
        case 2:
            print("Eliminar cliente".center(100,"="))
            cid = input("Client ID que desea eliminar:\t")
            if cid not in clients_db:
                print("No existe el cliente en la base datos".upper().center(100))
            else:
                clients_db.pop(cid)
                print("Se ha eliminado Client ID: {} con exito".upper().center(100).format(cid))
    
        case 3:
            print("Mostrar cliente".center(100,"="))
            cid = input("Client ID que desea ver:\t")
            
            if cid not in clients_db:
                print("No existe el cliente en la base de datos".upper().center(100))
            else:
                print(f"Client ID:\t{cid}")
                print(f"Nombre:\t{clients_db[cid]['name']}")
                print(f"Direccion:\t{clients_db[cid]['address']}")
                print(f"Telefono:\t{clients_db[cid]['phone']}")
                print(f"Correo:\t{clients_db[cid]['mail']}")
                print(f"VIP:\t{str(clients_db[cid]['status'])}")

        case 4:
            print("Lista de clientes".center(100,"="))
            if len(clients_db) == 0:
                print("No existen clientes en la base de datos".upper().center(100))
            else:
                for ncid in clients_db:
                    print("=".center(100,"="))
                    print(f"Client ID:\t{ncid}")
                    print(f"Nombre:\t{clients_db[ncid]['name']}")
                    print(f"Direccion:\t{clients_db[ncid]['address']}")
                    print(f"Telefono:\t{clients_db[ncid]['phone']}")
                    print(f"Correo:\t{clients_db[ncid]['mail']}")
                    print(f"VIP:\t{clients_db[ncid]['status']}")

        case 5:
            print("Lista de clientes preferentes".center(100,"="))
            vclients = 0
            for ncid in clients_db:
                if clients_db[ncid]["status"] == True:
                    print("=".center(100,"="))
                    print(f"Client ID:\t{ncid}")
                    print(f"Nombre:\t{clients_db[ncid]['name']}")
                    print(f"Direccion:\t{clients_db[ncid]['address']}")
                    print(f"Telefono:\t{clients_db[ncid]['phone']}")
                    print(f"Correo:\t{clients_db[ncid]['mail']}")
                    print(f"VIP:\t{clients_db[ncid]['status']}")
                    vclients += 1
            if vclients == 0:
                print("No hay clientes preferentes en la base de datos".upper().center(100))

        case 6:
            break