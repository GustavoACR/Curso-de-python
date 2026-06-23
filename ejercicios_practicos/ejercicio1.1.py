#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = 100 - dalto_curso/otros_cursos_min * 100
direferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
deferencia_con_promedio = 100 - dalto_curso/otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_removido = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_removido_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#mostrando las diferencia de duracion (ejercicio A)
print("------------------------")
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido") #devuelve 40.0, es decir que el curso de Dalto dura un 60% menos que el curso más corto de otros cursos
print(f"El curso de Dalto dura un {direferencia_con_max}% menos que el mas lento") #devuelve 78.57142857142857, es decir que el curso de Dalto dura un 21.42857142857143% menos que el curso más largo de otros cursos
print(f"El curso de Dalto dura un {deferencia_con_promedio}% menos que el promedio") #devuelve 62.5, es decir que el curso de Dalto dura un 37.5% menos que el curso promedio de otros cursos
print("------------------------")

#mostrando el porcentaje de tiempo vacio removido (ejercicio B)
print(f"El curso promedio elimina un {tiempo_vacio_removido}% de tiempo vacio") #devuelve 30.0, es decir que el curso de Dalto tiene un 30% menos de tiempo vacio que el curso promedio de otros cursos
print(f"El curso de Dalto elimina un {tiempo_vacio_removido_dalto}% de tiempo vacio") #devuelve 50.0, es decir que el curso de Dalto tiene un 50% menos de tiempo vacio que el curso de Dalto
print("------------------------")

#mostrando diferencias si los cursos duraran 10 horas (ejercicio C)
print(f"ver 10 horas del curso de Dalto equivale a ver {otros_cursos_promedio * 100  // dalto_curso / 10} horas del otros cursos") #devuelve 16.666666666666668, es decir que ver 10 horas del curso de Dalto equivale a ver 16.666666666666668 horas del curso más rápido de otros cursos
print(f"ver 10 horas de otros cursos equivale a ver {dalto_curso * 100  // otros_cursos_promedio / 10} horas del curso mas lento") #devuelve 46.666666666666664, es decir que ver 10 horas del curso de Dalto equivale a ver 46.666666666666664 horas del curso más lento de otros cursos
print("------------------------")

