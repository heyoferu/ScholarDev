def setDesc(costo, descuento):
    return costo - costo * descuento / 100
    
def setIVA(costo, percentage):

    return costo + costo * percentage / 100

def canastita(objeto, function):
    total = 0
    for costo, descuento in objeto.items():
        total += function(costo, descuento)
    return total
total_a = 0
total_b = 0

size = int(input("Cuantos objetos quieren agregar?:\t"))
for i in range(size):
    c = int(input("Costo del objeto:\t"))
    d = int(input("Descuento del objeto:\t"))
    total_a += canastita({c:d}, setDesc)
    total_b += canastita({c:d}, setIVA)


print('Precio con descuento ', total_a)
print('Precion con iva', total_b)