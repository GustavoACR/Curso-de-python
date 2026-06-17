cadena1 = "Hola soy Gustavo"
cadena2 = "y tengo 20 años"

resultado = cadena1.upper() #convierte la cadena a mayúsculas
resultado = cadena1.lower() #convierte la cadena a minúsculas
resultado = cadena1.split() #divide la cadena en una lista de palabras
resultado = cadena1.capitalize() #convierte la primera letra a mayúscula

#Buscar una cadena dentro de otra cadena, si no hay coincidencia devuelve -1
resultado = cadena1.find("Gustavo") #devuelve la posición de la primera aparición

resultado = cadena1.index("Gustavo") #devuelve la posición de la primera aparición, lanza una excepción si no se encuentra

resultado = cadena1.isnumeric() #devuelve True si todos los caracteres son numéricos

resultado = cadena1.isalpha() #devuelve True si todos los caracteres son alfabéticos

#devuelve la cantidad de veces que aparece una subcadena dentro de otra cadena
resultado = cadena1.count("o") #devuelve 3  

#devuelve cuantos caracteres tiene la cadena, len es una función que se puede usar con cualquier tipo de dato
resultado = len(cadena1) #devuelve 16

#verifica si una cadena empieza con una subcadena específica
resultado = cadena1.startswith("Hola") #devuelve True

#verifica si una cadena termina con una subcadena específica
resultado = cadena1.endswith("avo") #devuelve True

#reemplaza una subcadena por otra dentro de la cadena, si no encuentra la subcadena devuelve la cadena original
resultado = cadena1.replace("Gustavo", "Juan") #devuelve "Hola soy Juan"

#separar una cadena en una lista de palabras usando un separador específico
resultado = cadena1.split(" ") #devuelve ['Hola', 'soy', 'Gustavo']

print(resultado[1]) #devuelve "soy"
#muestra los métodos disponibles para el tipo de dato string