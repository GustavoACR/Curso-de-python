#creando diccionarios con dict(), los diccionarios son colecciones de pares clave-valor, las claves deben ser únicas y los valores pueden ser de cualquier tipo de dato
diccionario = dict(nombre="Gustavo", apellido="Castro", edad=20)

#las listas no pueden ser claves de un diciconario y usamos frozenset para meter un conjunto dentro de un diccionario, ya que los conjuntos no son hashables y no pueden ser claves de un diccionario
diccionario2 = {frozenset(["dato1", "dato2"]): "valor1", "dato3": "valor2"} #crea un diccionario con los elementos especificados, el conjunto inmutable se puede meter dentro de un diccionario como clave

#creando diccionario con fronkeys valor por defecto None, se puede especificar un valor por defecto diferente a None pasando un segundo argumento a fromkeys()
diccionario3 = dict.fromkeys(["nombre", "apellido", "edad"]) #crea un diccionario con las claves especificadas y valores None
#creando diccionario con fronkeys valor por defecto None, se puede especificar un valor por defecto diferente a algun valor pasando un segundo argumento a fromkeys()
diccionario4 = dict.fromkeys(["nombre", "apellido", "edad"], "valor por defecto") #crea un diccionario con las claves especificadas y valores "valor por defecto"   




print(diccionario) #muestra el diccionario, en este caso {'nombre': 'Gustavo', 'apellido': 'Castro', 'edad': 20}    
print(diccionario2) #muestra el diccionario, en este caso {frozenset({'dato1', 'dato2'}): 'valor1', 'dato3': 'valor2'}    
print(diccionario3) #muestra el diccionario, en este caso {'nombre': None, 'apellido': None, 'edad': None}    


print(diccionario4) #muestra el diccionario, en este caso {'nombre': 'valor por defecto', 'apellido': 'valor por defecto', 'edad': 'valor por defecto'}