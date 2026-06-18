#metodos de lista
#creando una lista con list() y agregando elementos a la lista con append()
lista = list([20, 56, 34, 2020]) #crea una lista con los elementos especificados

#devuelve el número de elementos en la lista
cantidad_elementos = len(lista) #devuelve 3

#agrega un elemento al final de la lista
lista.append(44) #agrega un elemento al final de la lista

#agrega un elemento en una posición específica de la lista, si la posición es mayor al número de elementos se agrega al final de la lista
lista.insert(1, 20) #agrega 20 en la posición 1

#agregando varios elementos a la lista con extend()
lista.extend([False, True]) #agrega varios elementos al final de la lista

#eliminando un elemento de la listo por su indice, si el índice es mayor al número de elementos lanza una excepción
lista.pop(-1) #-1 es el índice del último elemento de la lista, -2 para el antepenultimo y asi sucesivamente, pop() devuelve el elemento eliminado

#remueve un elemento de la lista por su value, si el value no se encuentra en la lista lanza una excepción
lista.remove(20) #remueve 20 de la lista

#elimina todos los elementos de la lista, la lista queda vacía
# lista.clear() #elimina todos los elementos de la lista

#ordena los elementos de la lista en orden alfabético, si la lista contiene elementos de diferentes tipos lanza una excepción
lista.sort() #ordena los elementos de la lista en orden alfabético 
lista.sort(reverse=True) #ordena los elementos de la lista en orden alfabético inverso  

#invierte el orden de los elementos de la lista, no ordena los elementos, solo invierte su orden
lista.reverse() #invierte el orden de los elementos de la lista     

#encontrando el índice de un elemento en la lista, si el elemento no se encuentra lanza una excepción
indice = lista.index(34) #devuelve el índice de la primera aparición de 34


print(lista) #muestra los métodos disponibles para el tipo de dato lista




