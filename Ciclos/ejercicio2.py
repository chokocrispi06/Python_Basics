var = int(input("Introduce la altura del triángulo (entero positivo): "))
for var2 in range(var):
    for var3 in range(var2+1):
        print("*", end="")
    print("")