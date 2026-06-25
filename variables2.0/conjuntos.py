#creando un conjunto con set(), los conjuntos no permiten elementos duplicados y no tienen un orden específico
conjunto = set(["dato1", "dato2", "dato1"]) #crea un conjunto con los elementos especificados, el elemento duplicado "dato1" se elimina

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"]) #crea un conjunto inmutable con los elementos especificados
conjunto2 = {conjunto1, "dato3"} #crea un conjunto con los elementos especificados, el conjunto inmutable se puede meter dentro de otro conjunto    


#print(conjunto2) #muestra el conjunto, en este caso {'dato1', 'dato2'}   


#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si un conjunto es un subconjunto de otro conjunto
resultado = conjunto2.issubset(conjunto1) #devuelve True si conjunto2 es un subconjunto de conjunto1, es decir, si todos los elementos de conjunto2 están en conjunto1
resultado = conjunto2 <= conjunto1 #devuelve True si conjunto2 es un subconjunto de conjunto1, es decir, si todos los elementos de conjunto2 están en conjunto1 

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1) #devuelve True si conjunto1 es un superconjunto de conjunto2, es decir, si todos los elementos de conjunto2 están en conjunto1
resultado = conjunto2 > conjunto1 #devuelve True si conjunto2 es un superconjunto de conjunto1, es decir, si todos los elementos de conjunto1 están en conjunto2

#verificar si hay un numero en común entre los dos conjuntos
resultado = conjunto2.isdisjoint(conjunto1) #devuelve True si no hay elementos


print(resultado) #muestra el resultado, en este caso True