print("------------------------") #separador

frutas = ["papas", "batatas", "yuca", "camote", "malanga"] #crea una lista con los elementos especificados
cadena = "Hola, mundo!"
numeros = [1, 2, 3, 4, 5] #crea una lista con los elementos especificados
for fruta in frutas: #itera sobre los elementos de la lista frutas
    if fruta == "yuca": #si el elemento actual es "yuca", se salta a la siguiente iteración
        continue #salta a la siguiente iteración del bucle
    print(f"La fruta es {fruta}") #muestra cada elemento de la lista frutas, en este caso La fruta es papas, La fruta es batatas, La fruta es yuca, La fruta es camote, La fruta es malanga

print("------------------------") #separador
for fruta in frutas: #itera sobre los elementos de la lista frutas
    if fruta == "yuca": #si el elemento actual es "yuca", se salta a la siguiente iteración
        break #termina el bucle, no se ejecuta el resto del código dentro del bucle
    print(f"La fruta es {fruta}") #muestra cada elemento de la lista frutas, en este caso La fruta es papas, La fruta es batatas, La fruta es yuca, La fruta es camote, La fruta es malanga


print("------------------------") #separador

#recorrer una cadena de texto

for caracter in cadena: #itera sobre los caracteres de la cadena
    print(f"El caracter es {caracter}") #muestra cada caracter de la cadena, en este caso El caracter es H, El caracter es o, El caracter es l, El caracter es a, El caracter es ,, El caracter es , El caracter es m, El caracter es u, El caracter es n, El caracter es d, El caracter es o, El caracter es !
    
print("------------------------") #separador
#for en una sola linea, se puede usar una expresión generadora para crear una lista de los caracteres de la cadena
numeros_duplicados = [x*2 for x in numeros] #crea una lista con los números de la lista, en este caso [2, 4, 6, 8, 10]
print(numeros_duplicados) #muestra la lista de números duplicados, en este caso [2, 4, 6, 8, 10]
