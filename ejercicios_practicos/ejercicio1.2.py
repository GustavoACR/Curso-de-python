frase = input("Ingrese una frase: ") #pide un dato al usuario y lo guarda
palabras_separadas = frase.split(" ") #divide la frase en palabras y cuenta la cantidad de palabras
cantidad_palabras = len(palabras_separadas) #cuenta la cantidad de palabras 
print(f"La frase ingresada tiene {cantidad_palabras} palabras y tardarias {cantidad_palabras / 2} segundos en decirlo") #muestra la cantidad de palabras
print(f"Dalto lo diria en {cantidad_palabras / 2 * 1.3} segundos") #muestra la cantidad de palabras

if cantidad_palabras > 20: #si la cantidad de palabras es mayor a 20, muestra un mensaje de advertencia
    print("La frase ingresada es muy larga, se recomienda dividirla en varias frases") #muestra un mensaje de advertencia
