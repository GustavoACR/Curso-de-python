#CREANDO FUNCIONES PROPIAS

#creando una funcion simple que no recibe parámetros y no retorna ningún valor
def saludar(): #crea una función que recibe un parámetro nombre
    print("hola como estas?") #muestra un mensaje de saludo con el nombre ingresado

#saludar() #llama a la función saludar, en este caso muestra el mensaje "hola como estas?"

#creando una funcion que recibe un parámetro
def saludar(nombre, sexo): #crea una función que recibe un parámetro nombre
    sexo = sexo.lower() #convierte el valor del parámetro sexo a minúsculas
    
    if (sexo == "mujer"):
        adjetivo = "reina"
        
    elif (sexo == "hombre"):
        adjetivo = "rey"
        
    else:
        adjetivo = "persona"
        
    print(f"hola {nombre}, como estas? mi {adjetivo}") #retorna un mensaje de saludo con el nombre ingresado

saludar("Gustavo", "hombre") #llama a la función saludar, en este caso muestra el mensaje "hola Gustavo, como estas? mi rey"
saludar("Gustava", "mujer") #llama a la función saludar, en este caso muestra el mensaje "hola Gustavo, como estas? mi reina"
saludar("Gustave", "otro") #llama a la función saludar,


#creando una funcion que recibe un parámetro y retorna multiples valores

def contraseña_random(num):
    chars = "abcdefghij"
    
    num_entero = str(num) #convierte el número a string
    num = int(num_entero[0]) #toma el primer dígito y convierte el número a entero
    
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" #concatena los caracteres correspondientes a los índices c1, c2 y c3 de la cadena chars
    return contraseña, num #retorna la contraseña generada
    
#desempaquetando los valores retornados por la función contraseña_random en dos variables
password, num = contraseña_random(25) #llama a la función contraseña_random, en este caso muestra la contraseña generada

print(f"La contraseña generada es: {password}") #muestra la contraseña generada, en este caso La contraseña generada es: cge10
print(f"El número utilizado es: {num}") #muestra el número utilizado, en este caso El número utilizado es: 2
