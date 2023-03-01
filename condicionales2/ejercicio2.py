#2. Escribir una función que reciba una cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
#minúsculas.

Pablo = "holaa"
Pablo = input("Introduce la contraseña: ")
def clave (password):
    if(Pablo == password.lower()):
        print("el password esta correcto")
    else:
        print("no hay coincidencia en el password")
        
        
        
        
clave("holaa")