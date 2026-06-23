#pedirle un numero al usuario y mostrarlo en pantalla, el dato ingresado es de tipo string, por lo que hay que convertirlo a int o float para poder hacer operaciones matemáticas   
numero = input("Ingrese un número: ") #pide un dato al usuario y lo guarda
#numero = int(numero) #convierte el dato ingresado a int
numero = float(numero) #convierte el dato ingresado a float

resultado = numero * 2 #multiplica el número ingresado por 2    

print(f"El resultado es {resultado}") #muestra el resultado de la operación 

