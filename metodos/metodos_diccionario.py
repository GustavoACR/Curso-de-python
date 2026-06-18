#metodos de diccionario

diccionario = {
    "nombre": "Gustavo", 
    "edad": 20, 
    "ciudad": "Nogales"
} #crea un diccionario con los elementos especificados

claves = diccionario.keys() #devuelve una lista con las claves del diccionario  
#los keys tambien se usan para iterar sobre los elementos del diccionario, por ejemplo: for clave in diccionario.keys(): print(clave)

valor_nombre = diccionario.get("nombre") #devuelve el valor de la clave especificada, si la clave no existe devuelve None
#tambien se puede llamar por numero de índice, por ejemplo: diccionario.get(0) devuelve el valor de la primera clave del diccionario

#eliminando todos los elementos del diccionario, el diccionario queda vacío
# diccionario.clear() #elimina todos los elementos del diccionario

#eliminando un elemento del diccionario por su clave, si la clave no existe lanza una excepción
diccionario.pop("edad") #elimina el elemento con la clave especificada y devuelve

#obteniendo un elemento dict_items iterable con los elementos del diccionario, cada elemento es una tupla con la clave y el valor
elementos = diccionario.items() #devuelve un dict_items iterable con los elementos del dic

print(elementos) #muestra los métodos disponibles para el tipo de dato diccionario 


