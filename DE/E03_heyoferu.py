box = []

temp = input("inserter valores separados por coma: ")

box = temp.split(',')
print(box)
tuple((box))

s = 0
for c in range(len(box)):
    s += float(box[c])

media = s/len(box)

z = 0
for i in range(len(box)):
    z += (float(box[i])-media)**2

pre_desv = z/len(box)

desv = pre_desv**0.5

print(f"Media: {media}")
print(f"Desviacion media: {desv}")