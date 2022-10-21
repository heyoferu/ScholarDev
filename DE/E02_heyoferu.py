a = (
    (1,2,3),
    (4,5,6)
)

b = (
    (-1,0),
    (0,1),
    (1,1)
)

c = [
    [0,0],
    [0,0]
]

# for i in range(3):
#     for j in range(3):
#         temp = a[0][i] * b[j][0]
#         print(temp)

# for fila in range(3):
#     temp += a[1][fila] * b[fila][1]

# for ops in range(4):
#     for columna,fila in range(3):
#         temp += a[0][columna] * b[fila][0]

# for afila in range(2):
#     for bcolumna in range(2):
#         temp = 0
#         for coef in range(3):
#             temp += a[afila][coef] * b[coef][bcolumna]
#         print(temp)
#         c.append(temp)


for afila in range(2):
    for bcolumna in range(2):
        temp = 0
        for coef in range(3):
            temp += a[afila][coef] * b[coef][bcolumna]
        c[afila][bcolumna] = temp

for matrix in range(len(c)):
    print(f"{c[matrix][0]} {c[matrix][1]}".center(50))