#iterar listas con for, se puede usar un bucle for para iterar sobre los elementos de una lista, tupla, conjunto o diccionario
#lista = ["dato1", "dato2", "dato3"]
animales = ["perro", "gato", "conejo", "loro", "pez"]
numeros = [1, 2, 3, 4, 5]
#recorriendo la lista animales
for animal in animales: #itera sobre los elementos de la lista animales
    print(animal) #muestra cada elemento de la lista animales, en este caso perro, gato, conejo, loro, pez

#recorriendo la lista numeros
for numero in numeros: #itera sobre los elementos de la lista numeros
    resultado = numero * 2 #multiplica cada elemento de la lista numeros por 2  
    print(resultado) #muestra cada elemento de la lista numeros, en este caso 1, 2, 3, 4, 5


#itera sobre los elementos de las listas numeros y animales al mismo tiempo, zip() devuelve un iterador de tuplas, cada tupla contiene un elemento de cada lista
#tienen que tener la misma cantidad de elementos, si no, se detiene en el elemento que no tiene pareja
# for numeros, animales in zip(numeros, animales): #itera sobre los elementos de las listas numeros y animales al mismo tiempo, zip() devuelve un iterador de tuplas, cada tupla contiene un elemento de cada lista
#     print(f"El animal {animales} tiene el número {numeros}") #muestra cada elemento de las listas numeros y animales, en este caso El animal perro tiene el número 1, El animal gato tiene el número 2, El animal conejo tiene el número 3, El animal loro tiene el número 4, El animal pez tiene el número 5   
  
  
#recorriendo una lista por el indice usando range  (no optima) (NO FUNCIONA EN CONJUNTOS)
for num in range(5, 10): #itera sobre los números del 5 al 9, range() devuelve un iterador de números enteros
    print(num) #muestra cada número del 5 al 9, en este caso 5, 6, 7, 8, 9
    
for num in range(len(animales)): #itera sobre los índices de la lista animales, len() devuelve la cantidad de elementos de la lista
    print(f"El animal {animales[num]} tiene el número {num}") #muestra cada elemento de la lista animales y su índice, en este caso El animal perro tiene el número 0, El animal gato tiene el número 1, El animal conejo tiene el número 2, El animal loro tiene el número 3, El animal pez tiene el número 4    

print("------------------------") #separador

#forma correcta de recorrer una lista por el indice usando enumerate(), enumerate() devuelve un iterador de tuplas, cada tupla contiene un índice y un elemento de la lista
for num in enumerate(numeros): #itera sobre los elementos de la lista numeros y sus índices, enumerate() devuelve un iterador de tuplas, cada tupla contiene un índice y un elemento de la lista
    #print(f"El animal {animales[num[0]]} tiene el número {num[1]}") #muestra cada elemento de las listas numeros y animales, en este caso El animal perro tiene el número 1, El animal gato tiene el número 2, El animal conejo tiene el número 3, El animal loro tiene el número 4, El animal pez tiene el número 5    
    indice = num[0] #guarda el índice del elemento actual
    valor = num[1] #guarda el valor del elemento actual
    print(f"El índice del elemento actual es {indice} y el valor es {valor}") #muestra el índice y el valor del elemento actual, en este caso El índice del elemento actual es 0 y el valor es 1, El índice del elemento actual es 1 y el valor es 2, El índice del elemento actual es 2 y el valor es 3, El índice del elemento actual es 3 y el valor es 4, El índice del elemento actual es 4 y el valor es 5
    
print("------------------------") #separador

for indice, valor in enumerate(animales): #itera sobre los elementos de la lista animales y sus índices, enumerate() devuelve un iterador de tuplas, cada tupla contiene un índice y un elemento de la lista
    print(f"El índice del elemento actual es {indice} y el valor es {valor}") #muestra el índice y el valor del elemento actual, en este caso El índice del elemento actual es 0 y el valor es perro, El índice del elemento actual es 1 y el valor es gato, El índice del elemento actual es 2 y el valor es conejo, El índice del elemento actual es 3 y el valor es loro, El índice del elemento actual es 4 y el valor es pez
    
print("------------------------") #separador
#usando el else
for num in numeros: #itera sobre los elementos de la lista numeros
    print(f"El número actual es {num}") #muestra cada elemento de la lista numeros, en este caso El número actual es 1, El número actual es 2, El número actual es 3, El número actual es 4, El número actual es 5
else:
    print("Se han recorrido todos los elementos de la lista numeros") #muestra un mensaje cuando se han recorrido todos los elementos de la lista numeros
    
#todo lo anterio funciona para las tuplas, conjuntos y diccionarios, en el caso de los diccionarios se itera sobre las claves del diccionario, para iterar sobre los valores o los pares clave-valor se puede usar el método items() del diccionario