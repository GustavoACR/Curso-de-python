print("------------------------") #separador

diccionario = {
    "nombre": "Gustavo", 
    "apellido": "Castro", 
    "edad": 20
} #crea un diccionario con los elementos especificados

for datos in diccionario.items(): #itera sobre los pares clave-valor del diccionario
    key = datos[0] #guarda la clave del elemento actual
    value = datos[1] #guarda el valor del elemento actual
    
    print(f"La clave es {key} y el valor es {value}") #muestra cada clave y su valor

print("------------------------") #separador

for key, value in diccionario.items(): #itera sobre los pares clave-valor del diccionario
    print(f"La clave es {key} y el valor es {value}") #muestra cada clave y su valor
    
print("------------------------") #separador

for key in diccionario: #itera sobre las claves del diccionario
    print(f"La clave es {key} y el valor es {diccionario[key]}") #muestra cada clave y su valor
