#creando una lista que se puede modificar
lista = ["gustavo castro", "soy gustavo", True, 1.72]

#creando una lista que no se puede modificar
tupla = ("gustavo castro", "soy gustavo", True, 1.7)

#esto es valido
lista[3] = "kaka"

#esto no es valido
#tupla[3] = "kaka"

#creando un conjusto (set)
#no se pueden llamar a sus elementos por indice solo por un bucle
#en un conjuto no se pueden poner duplicados
conjunto = {"gustavo castro", "soy gustavo", True, 1.7}

#print(conjunto[1]) #no se puede accerder al elemento

#creando un diccionario (dict) la estructura es key : value separado por comas
diccionario = {
    'nombre' : "gustavo castro",
    'canal' : "de las estrellas",
    'esta_emocionado' : True,
    'altura': 1.72,
    'dato_duplicado' : "gustavo castro"
}

print(diccionario["nombre"])