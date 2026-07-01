def frase(nombre, apellido,adjetivo):
    return f"{nombre} {apellido} es un {adjetivo}" #retorna una frase con el nombre, apellido y adjetivo recibidos como argumentos  

frase_resultado = frase(adjetivo="programador", apellido="Castro",nombre="Gustavo") #llama a la función frase, en este caso muestra la frase generada
print(f"La frase generada es: {frase_resultado}") #muestra la frase

#creando una funcion con un parametro opcional, y un valor por defecto
def frase(nombre, apellido,adjetivo="genio"):
    return f"{nombre} {apellido} es un {adjetivo}" #retorna una frase con el nombre, apellido y adjetivo recibidos como argumentos  

frase_resultado = frase("Gustavo", "Castro", "perro") #llama a la función frase, en este caso muestra la frase generada
print(f"La frase generada es: {frase_resultado}") #muestra la frase
