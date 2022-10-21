def iva_fact(costo):
    iva=16
    total = costo + costo*iva/100
    return total
    
factura = int(input("Valor de la factura:\t"))
print("Total con iva:",iva_fact(factura))