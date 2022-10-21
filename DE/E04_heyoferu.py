facturas = {
    "pendientes":{
        "clave":[],
        "importe":[]
    },
    "pagadas":{
        "clave":[],
        "importe":[]
    }
}

cant_p = 0
cant_d = 0

def showFacts():
    sumd = 0
    sump = 0
    print("\nMostrando datos...\n")
    print("\nADEUDOS...")
    for i in range(len(facturas["pendientes"]["clave"])):
        print(f"{i+1}) Factura: {facturas['pendientes']['clave'][i]} Importe: {facturas['pendientes']['importe'][i]}")
        sumd += facturas["pendientes"]["importe"][i]

    restd = len(facturas["pendientes"]["clave"])
    print(f"Cuentas por cobrar: {restd}")
    print(f"Total por cobrar: {sumd}")   

    print("\nPAGADAS")
    for i in range(len(facturas["pagadas"]["clave"])):
        print(f"{i+1}) Factura: {facturas['pagadas']['clave'][i]} Importe: {facturas['pagadas']['importe'][i]}")
        sump += facturas["pagadas"]["importe"][i]

    restp = len(facturas["pagadas"]["clave"])
    print(f"Cuentas pagadas: {restp}")
    print(f"Total pagado: {sump}")

menu = ["Agregar","Pagar","Salir"]
while True:
    print("\n")
    print("Facturas y cuentas".center(70,"="))
    for i in range(3):
        print(f"{i+1}) {menu[i]}")

    selection = int(input("Seleccione una opcion: "))
    match selection:
        case 1:
            facturas["pendientes"]["clave"].append(input("Agregar clave, identificador o numero de factura: "))
            facturas["pendientes"]["importe"].append(int(input("Agregar importe de factura: ")))
            showFacts()

        case 2:
            while True:
                if len(facturas["pendientes"]["clave"]) == 0:
                    print("No hay facturas por pagar")
                    break
                
                else:                    
                    print("Que factura desea pagar")
                    for i in range(len(facturas["pendientes"]["clave"])):
                        print(f"{i+1}) Factura: {facturas['pendientes']['clave'][i]} Importe: {facturas['pendientes']['importe'][i]}")
                    nfact = int(input("Numero de factura: "))

                    facturas["pagadas"]["clave"].append(facturas['pendientes']['clave'][nfact-1])
                    facturas["pagadas"]["importe"].append(facturas['pendientes']['importe'][nfact-1])
                    
                    facturas["pendientes"]["clave"].pop(nfact-1)
                    facturas["pendientes"]["importe"].pop(nfact-1)

                    showFacts()
        
        case 3:
            print("Gracias por usar el programa Banco de Fer")
            break