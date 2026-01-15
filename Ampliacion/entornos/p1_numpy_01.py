import numpy as np
import time

'''
https://numpy.org/doc/stable/
https://numpy.org/es/learn/
https://deepnote.com/app/anthonymanotoa/Tutorial-de-NumPy-en-Espanol-180f7d51-b297-4aea-b61e-34ef867ca6fb
https://www.w3schools.com/python/numpy/default.asp
https://realpython.com/numpy-tutorial/
'''

def ejemplo1():
	print("Medicion de rencimiento con respecto a listas normales")
	#Ejemplo de rendimiento
	# Ejemplo con listas
	lista = list(range(1000000))
	start = time.time()
	sum(lista)
	print("Lista:", time.time() - start)

	# Ejemplo con arrays
	arr = np.arange(1000000)
	start = time.time()
	np.sum(arr)
	print("Array:", time.time() - start)
    

def creacionArrays():

    # Array de una dimensión
    a1 = np.array([1, 2, 3])
    print(a1)
    print(a1[1])
    print("-"*25)
    
    # Array de dos dimensiones (matriz)
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(a2)
    print(a2[0])
    print(a2[0][2])
    print("-"*25)
    
    # Array de 3 dimensiones
    a3 = np.zeros((5, 4, 3))
    print(a3)
    print("-"*25)
    
    for i in a2:
        for j in i:
            print(j,end="")
        print()
        
def algunasPropiedades():
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(a2)
    print("Shape:", a2.shape)
    print("Shape:", a2.shape[0])
    print("Shape:", len(a2))
    print("Shape:", a2.shape[1])
    print("Número de dimensiones:", a2.ndim)
    print("Número de elementos:", a2.size)
    print("Número de elementos:", len(a2))
    print("Tipo de dato:", a2.dtype)
    print("Tamaño de cada elemento:", a2.itemsize)
    print("Tamaño total en bytes:", a2.nbytes)

def ejercicio1():
    a3 = np.zeros((5, 4))
    print(a3)
    print("-"*25)
    #RELLENA LOS ELEMENTOS DE LA MATRIZ CON LOS NUMEROS DEL 1 AL 20
    print(a3)
    
def operacionesBasicas():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", b / a)
    print("FUNCIONES MATEMATICAS")
    print("Media:", np.mean(a))    
    print("Máximo:", np.max(a))
    print("Mínimo:", np.min(a))
    print("Desviación estándar:", np.std(a))
    print("Suma:", np.sum(a))


print("Empezamos")
print("Version:",np.__version__)

# ejemplo1()
# print("*"*50)
# creacionArrays()
# print("*"*50)
# algunasPropiedades()
# print("*"*50)
# ejercicio1()
# print("*"*50)
# operacionesBasicas()

print("Fin")

import numpy as np
import time

def ejercicio1():
    print("EJERCICIO 1: Array 1D del 0 al 9")
    a1 = np.arange(10)
    print(a1)
    print("-" * 25)

def ejercicio2():
    print("EJERCICIO 2: Array de ceros (3, 4)")
    a2 = np.zeros((3, 4))
    print(a2)
    print("-" * 25)

def ejercicio3():
    print("EJERCICIO 3: Array de unos (5, 2) int32")
    a3 = np.ones((5, 2), dtype=np.int32)
    print(a3)
    print("-" * 25)

def ejercicio4():
    print("EJERCICIO 4: 21 elementos entre 0 y 100")
    a4 = np.linspace(0, 100, 21)
    print(a4)
    print("-" * 25)

def ejercicio5():
    print("EJERCICIO 5: 50 valores aleatorios entre 0 y 1")
    a5 = np.random.random(50)
    print(a5)
    print("-" * 25)

def ejercicio6():
    print("EJERCICIO 6: Convertir a float64")
    arr = np.array([1, 2, 3, 4, 5])
    a6 = arr.astype(np.float64)
    print(a6, a6.dtype)
    print("-" * 25)

def ejercicio7():
    print("EJERCICIO 7: Matriz identidad 6x6")
    a7 = np.eye(6)
    print(a7)
    print("-" * 25)

def ejercicio8():
    print("EJERCICIO 8: Array del 10 al 49")
    a8 = np.arange(10, 50)
    print(a8)
    print("-" * 25)

def ejercicio9():
    print("EJERCICIO 9: Invertir con np.flip")
    a8 = np.arange(10, 50)
    a9 = np.flip(a8)
    print(a9)
    print("-" * 25)

def ejercicio10():
    print("EJERCICIO 10: Índices de elementos no cero")
    arr = np.array([0, 2, 0, 5, 0, 8, 0])
    a10 = np.nonzero(arr)
    print(a10)
    print("-" * 25)

def ejercicio11():
    print("EJERCICIO 11: Reshape a (3, 4)")
    a11 = np.arange(12).reshape((3, 4))
    print(a11)
    print("-" * 25)

def ejercicio12():
    print("EJERCICIO 12: Matriz 5x5 y submatriz central 3x3")
    m = np.arange(1, 26).reshape(5, 5)
    sub = m[1:4, 1:4]
    print("Original:\n", m)
    print("Central 3x3:\n", sub)
    print("-" * 25)

def ejercicio13():
    print("EJERCICIO 13: Marco de 1s en array de ceros")
    a13 = np.zeros((4, 4))
    a13[0, :] = 1; a13[-1, :] = 1
    a13[:, 0] = 1; a13[:, -1] = 1
    print(a13)
    print("-" * 25)

def ejercicio14():
    print("EJERCICIO 14: Tablero de ajedrez 8x8")
    a14 = np.zeros((8, 8), dtype=int)
    a14[1::2, ::2] = 1
    a14[::2, 1::2] = 1
    print(a14)
    print("-" * 25)

def ejercicio15():
    print("EJERCICIO 15: Concatenación H y V")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    h = np.concatenate((a, b)) # Horizontal (1D)
    v = np.vstack((a, b))      # Vertical
    print("Horizontal:", h)
    print("Vertical:\n", v)
    print("-" * 25)

def ejercicio16():
    print("EJERCICIO 16: Pares +5, Impares -3")
    arr = np.array([1, 2, 3, 4, 5, 6])
    res = np.where(arr % 2 == 0, arr + 5, arr - 3)
    print(res)
    print("-" * 25)

def ejercicio17():
    print("EJERCICIO 17: Clip valores (10, 30)")
    arr = np.random.randint(0, 51, 100)
    res = np.clip(arr, 10, 30)
    print(res)
    print("-" * 25)

def ejercicio18():
    print("EJERCICIO 18: Media, Mediana y Desviación")
    arr = np.random.normal(0, 1, 1000)
    print(f"Media: {np.mean(arr):.2f}, Mediana: {np.median(arr):.2f}, Std: {np.std(arr):.2f}")
    print("-" * 25)

def ejercicio19():
    print("EJERCICIO 19: Normalización")
    arr = np.array([10, 20, 30, 40, 50])
    norm = (arr - np.mean(arr)) / np.std(arr)
    print(norm)
    print("-" * 25)

def ejercicio20():
    print("EJERCICIO 20: Máximo y posición por fila")
    m = np.random.random((6, 6))
    max_vals = np.max(m, axis=1)
    posiciones = np.argmax(m, axis=1)
    print("Maximos:", max_vals)
    print("Posiciones:", posiciones)
    print("-" * 25)

def ejercicio21():
    print("EJERCICIO 21: Broadcasting suma vector a matriz")
    m = np.zeros((10, 5))
    v = np.array([1, 2, 3, 4, 5])
    res = m + v
    print(res)
    print("-" * 25)

def ejercicio22():
    print("EJERCICIO 22: Producto matricial @")
    a = np.random.random((3, 3))
    b = np.random.random((3, 3))
    res = a @ b
    print(res)
    print("-" * 25)

def ejercicio23():
    print("EJERCICIO 23: Diagonales de 10x10")
    m = np.arange(100).reshape(10, 10)
    diag = np.diagonal(m)
    arriba = np.diagonal(m, offset=1)
    abajo = np.diagonal(m, offset=-1)
    print("Principal:", diag)
    print("Arriba:", arriba)
    print("Abajo:", abajo)
    print("-" * 25)

def ejercicio24():
    print("EJERCICIO 24: Redondeo al más cercano")
    arr = np.random.uniform(0, 10, 20)
    res = np.round(arr)
    print("Original:", arr[:5])
    print("Redondeado:", res[:5])
    print("-" * 25)

def ejercicio25():
    print("EJERCICIO 25: Suma eje 1 en (6, 7, 8)")
    arr = np.ones((6, 7, 8))
    res = np.sum(arr, axis=1)
    print("Shape resultado:", res.shape)
    print("-" * 25)

def ejercicio26():
    print("EJERCICIO 26: Valores únicos y conteos")
    arr = np.array([1, 2, 1, 3, 2, 4, 5, 2, 3, 1, 5, 5])
    valores, conteos = np.unique(arr, return_counts=True)
    print("Valores:", valores)
    print("Conteos:", conteos)
    print("-" * 25)

def ejercicio27():
    print("EJERCICIO 27: np.where (1 si > 0.5, sino -1)")
    arr = np.random.random(10)
    res = np.where(arr > 0.5, 1, -1)
    print("Array:", arr)
    print("Resultado:", res)
    print("-" * 25)

def ejercicio28():
    print("EJERCICIO 28: Distancia Euclidiana")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    dist = np.sqrt(np.sum((a - b)**2))
    print("Distancia:", dist)
    print("-" * 25)

def ejercicio29():
    print("EJERCICIO 29: Punto más cercano al origen")
    puntos = np.random.uniform(-10, 10, (1000, 2))
    distancias = np.sqrt(np.sum(puntos**2, axis=1))
    indice_min = np.argmin(distancias)
    print(f"Punto más cercano: {puntos[indice_min]} a distancia {distancias[indice_min]:.4f}")
    print("-" * 25)

def ejercicio30():
    print("EJERCICIO 30: Columnas pares cuadrado, impares raíz")
    m = np.random.randint(1, 100, (10, 10)).astype(float)
    m[:, 0::2] = m[:, 0::2]**2
    m[:, 1::2] = np.sqrt(m[:, 1::2])
    print(m[:2, :4]) # Muestra una parte
    print("-" * 25)

ejercicio1()    
ejercicio2()    
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio6()
ejercicio7()
ejercicio8()
ejercicio9()
ejercicio10()
ejercicio11()
ejercicio12()
ejercicio13()
ejercicio14()
ejercicio15()
ejercicio16()
ejercicio17()
ejercicio18()
ejercicio19()
ejercicio20()
ejercicio21()
ejercicio22()
ejercicio23()
ejercicio24()
ejercicio25()
ejercicio26()
ejercicio27()
ejercicio28()
ejercicio29()
ejercicio30()
   

'''

Ejercicios numpy

### Nivel Básico (1-10)
1. Crea un array 1D de 10 elementos con valores del 0 al 9.  
2. Crea un array de ceros de forma (3, 4).  
3. Crea un array de unos de forma (5, 2) con tipo de dato `int32`.  
4. Crea un array con valores espaciados uniformemente entre 0 y 100 (inclusive) con 21 elementos.  
5. Crea un array 1D con 50 valores aleatorios entre 0 y 1 (usa `np.random.random`).  
6. Convierte el siguiente array a tipo `float64`: `arr = np.array([1, 2, 3, 4, 5])`  
7. Crea una matriz identidad 6×6.  
8. Crea un array 1D con valores del 10 al 49 (ambos incluidos).  
9. Invierte el orden de los elementos del array anterior (sin usar `[::-1]`). Usa `np.flip`.  
10. Encuentra los índices de los elementos no cero en: `arr = np.array([0, 2, 0, 5, 0, 8, 0])`

### Nivel Básico-Intermedio (11-20)
11. Cambia la forma del array `np.arange(12)` a (3, 4) sin cambiar sus datos.  
12. Crea una matriz 5×5 con valores de 1 a 25 y luego extrae la submatriz central 3×3.  
13. Crea un array 4×4 de ceros y pon 1s en el borde (como un marco).  
14. Crea un array de forma (8, 8) con un patrón de tablero de ajedrez (0s y 1s alternados).  
15. Dados `a = np.array([1,2,3])` y `b = np.array([4,5,6])`, concaténalos horizontal y verticalmente.  
16. Sin usar bucles, suma 5 a todos los elementos pares de un array y resta 3 a los impares.  
17. Reemplaza todos los valores mayores que 30 por 30 y menores que 10 por 10 en un array aleatorio de 100 elementos entre 0 y 50.  
18. Calcula la media, mediana y desviación estándar de un array de 1000 números aleatorios normales.  
19. Normaliza (resta la media y divide por la desviación estándar) un array 1D.  
20. Encuentra el valor máximo y su posición en cada fila de una matriz 6×6 de números aleatorios.

### Nivel Intermedio (21-30)
21. Usa broadcasting para sumar un vector fila a cada fila de una matriz 10×5.  
22. Crea dos matrices 3×3 aleatorias y calcula su producto matricial (usa `@` o `np.matmul`).  
23. Dada una matriz 10×10, extrae la diagonal principal y las dos diagonales por encima y debajo de ella.  
24. Genera un array 1D de 20 elementos y redondea cada elemento al entero más cercano.  
25. Crea un array de forma (6, 7, 8) y calcula la suma a lo largo del eje 1.  
26. Encuentra los valores únicos y sus conteos en el array:  
   `arr = np.array([1,2,1,3,2,4,5,2,3,1,5,5])`  
27. Usa `np.where` para crear un array que sea 1 donde los valores sean mayores que 0.5 y -1 en caso contrario (sobre un array aleatorio).  
28. Implementa la función de distancia euclidiana entre dos arrays 1D sin usar bucles ni `np.linalg.norm`.  
29. Genera 1000 puntos aleatorios en 2D (matriz 1000×2) y encuentra cuál está más cerca del origen (0,0).  
30. Crea una matriz 100×100 y reemplaza todos los elementos de las columnas pares por sus valores al cuadrado y los de las columnas impares por su raíz cuadrada.
'''
