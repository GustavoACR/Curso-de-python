#forma no optima de suma valores
def suma(lista):
    numeros_sumados = 0 #inicializa la variable que almacenará la suma de los números 
    
    for numero in lista: #itera sobre los elementos de la lista
        numeros_sumados = numeros_sumados + numero #suma el número actual a la variable que almacena la suma de los números
    return numeros_sumados #retorna la suma de los números

resultado = suma([5, 10, 15]) #llama a la función suma, en este caso muestra el resultado de la suma de 5 y 10
print(f"El resultado de la suma no optimaes: {resultado}") #muestra el resultado de la suma, en este caso El resultado de la suma es: 15


#forma optima de suma valores
def suma(numeros):
    return sum([*numeros]) #retorna la suma de los números recibidos como argumentos, usando la función sum() que devuelve la suma de todos los valores de una lista de números

resultado = suma([5, 10, 15]) #llama a la función suma, en este caso muestra el resultado de la suma de 5 y 10
print(f"El resultado de la suma optima es: {resultado}") #muestra el resultado de la suma, en este caso El resultado de la suma es: 15


#utilizando el parametro *args para recibir una cantidad variable de argumentos
def suma(nombre, *numeros): #crea una función que recibe una cantidad variable de argumentos
    return f"{nombre}, la suma de tus números es: {sum(numeros)}" #retorna la suma de los números recibidos como argumentos

resultado = suma("Alice", 5, 10, 15) #llama a la función suma, en este caso muestra el resultado de la suma de 5, 10 y 15
print(f"El resultado de la suma optima con *args es: {resultado}") #muestra el resultado de la suma, en este caso El resultado de la suma es: 30
