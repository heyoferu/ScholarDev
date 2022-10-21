translator = {}
manu = ["Agregar palabras","Consultar palabra","Salir"]


while True:
    for i in range(len(manu)):
        print(f"{i+1}) {manu[i]}")
    mselect = int(input("Seleccione una:\t"))
    
    match mselect:
        case 1:
            words = input("Escriba las palabras en en el siguiente formato 'palabra:traduccion', si es mas de una, entonces use comillas\nPalabras:\t")
            for nword in words.split(','):
                palabra, traduccion = nword.split(':')
                translator[palabra] = traduccion

        case 2:
            find_palabra = input("Palabra:\t")
            for nword in translator:
                if find_palabra == str(nword):
                    print(f"Palabra: {palabra}\t|\tTraduccion: {translator[nword]}")
                else:
                    print(f"No existe {find_palabra}")
        
        case 3: 
            print("Goodbye")
