import time # Importar la libreria de time para medir el tiempo de ejecución 
import numpy as np # Importamos numpy para manejar mejor la creación de las matrices 
from tabulate import tabulate

# Definimos el tamaño de la matriz y estos se pueden modificar a otros números
alumnos = 500
materias = 6

# Creamos la matriz con datos aleatorios entre 0 y 100 
matriz = np.random.randint(0, 101, size=(alumnos, materias))

# Función para buscar el valor de una materia y un alumno en particular
# Se ajusta restando 1 porque los índices en Python comienzan desde 0
def buscar_alumno(matriz, alumno, materia):
    return matriz[alumno-1][materia-1], (alumno-1, materia-1)

inicio = time.time() 
for _ in range(100000): # Se realiza un ciclo que se repite 100,000 y el _ indica que no se necesita el valor de la variable 
    calificaciones, indices = buscar_alumno(matriz, 322, 6)
fin = time.time() 

datos = [
    ["Alumno", "Materia", "Calificación", "Posición"],
    [322, 6, calificaciones, indices]
]

# Mostramos los resultados
print("Matriz Alumno x Materia")
print(tabulate(datos, headers='firstrow', tablefmt='grid'))
print(f"Tiempo de ejecución de la búsqueda: {fin-inicio:.6f} segundos")