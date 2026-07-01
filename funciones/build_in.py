#FUNCIONES  
#encontrando el numero mayor de una lista de números, usando la función max() que devuelve el valor máximo de una lista de números

numeros = [2, 11, 3, 4, 5] #crea una lista con los elementos especificados

numero_mayor = max(numeros) #encuentra el número mayor de la lista
print(f"El número mayor es {numero_mayor}") #muestra el número mayor, en este caso El número mayor es 11 

#encontrando el numero menor de una lista de números, usando la función min() que devuelve el valor mínimo de una lista de números
numero_menor = min(numeros) #encuentra el número menor de la lista
print(f"El número menor es {numero_menor}") #muestra el número menor, en este caso El número menor es 2

#redondeando un número decimal a un número entero, usando la función round() que devuelve el valor redondeado de un número decimal
numero_decimal = 3.14159 #crea un número decimal
numero_redondeado = round(numero_decimal, 3) #redondea el número decimal
print(f"El número redondeado es {numero_redondeado}") #muestra el número redondeado, en este caso El número redondeado es 3.142

#retorna False si le argumento es 0, None, False, [], {}, "", y True en cualquier otro caso
valor = 1 #crea un valor
resultado_bool = bool(valor) #convierte el valor a booleano
#print(resultado_bool) #muestra el valor booleano del valor

#retorna true si todos los valores de la lista son verdaderos, y false si al menos uno es falso
valores = [1, 2, 3, 4, 5] #crea una lista con los elementos especificados
resultado_all = all(valores) #verifica si todos los valores de la lista son verdaderos
print(resultado_all) #muestra el valor booleano de la lista, en este caso True, ya que todos los valores de la lista son verdaderos

#suma todos los valores de una lista de números, usando la función sum() que devuelve la suma de todos los valores de una lista de números
suma_numeros = sum(numeros) #suma todos los valores de la lista de números
print(f"La suma de los números es {suma_numeros}") #muestra la suma de los números, en este caso La suma de los números es 24

