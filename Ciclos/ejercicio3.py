#3
var = int(input("Introduce la altura del triángulo (entero positivo): "))
for var2 in range(1, var+1, 2):
    for var3 in range(var2, 0, -2):
        print(var3, end=" ")
    print("")