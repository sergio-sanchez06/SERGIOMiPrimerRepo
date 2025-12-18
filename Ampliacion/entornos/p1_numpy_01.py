from entorno1.Lib.site-packages.numpy.conftest import dtype
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

def ejercicio1():

    print("EJERCICIO 1")
    print("-"*25)

    a1 = np.arange(10)
    print(a1)
    print("-"*25)

def ejercicio2():
    print("EJERCICIO 2")
    print("-"*25)

    a2 = np.zeros((3,4))
    print(a2)
    print("-"*25)

def ejercicio3():

    print("EJERCICIO 3")
    print("-"*25)
    a3 = np.ones((5,2), dtype=np.int32)
    print(a3)
    print("-"*25)

def ejercicio4():

    print("EJERCICIO 4")
    print("-"*25)
    a4 = np.linspace(0,100,21)
    print(a4)
    print("-"*25)

def ejercicio5():
    print("EJERCICIO 5")
    print("-"*25)
    a5 = np.random.random((3,4))
    print(a5)
    print("-"*25)

def ejercicio6():
    print("EJERCICIO 6")
    print("-"*25)
    a6 = np.array([1,2,3,4,5])
    a6 = a6.astype(np.float64)
    print(a6)
    print("-"*25)

def ejercicio7():
    print("EJERCICIO 7")
    print("-"*25)
    a7 = np.identity(6)
    print(a7)
    print("-"*25)

def ejercicio8():
    print("EJERCICIO 8")
    print("-"*25)
    a8 = np.arange(10,50)
    print(a8)
    print("-"*25)

def ejercicio9():
    print("EJERCICIO 9")
    print("-"*25)
    a9 = np.arange(10,50)
    a9 = np.flip(a9)
    print(a9)
    print("-"*25)

def ejercicio10():
    print("EJERCICIO 10")
    print("-"*25)
    a10 = np.array([0,2,0,5,0,8,0])
    a10 = np.nonzero(a10)
    print(a10)
    print("-"*25)

def ejercicio11():
    print("EJERCICIO 11")
    print("-"*25)
    a11 = np.arange(12)
    a11 = a11.reshape((3,4))
    print(a11)
    print("-"*25)

def ejercicio12():
    print("EJERCICIO 12")
    print("-"*25)
    a12 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    a12 = a12[1:2,1:2]
    print(a12)
    print("-"*25)

def ejercicio13():
    print("EJERCICIO 13")
    print("-"*25)
    a13 = np.zeros((4,4))
    a13[1:2,1:2] = 1
    print(a13)
    print("-"*25)

def ejercicio14():
    print("EJERCICIO 14")
    print("-"*25)
    a14 = np.zeros((8,8))
    a14[1::2,::2] = 1
    a14[::2,1::2] = 1
    print(a14)
    print("-"*25)

def ejercicio15():
    print("EJERCICIO 15")
    print("-"*25)
    a15 = np.array([1,2,3])
    a15 = np.concatenate((a15,a15))
    print(a15)
    print("-"*25)

def ejercicio16():
    print("EJERCICIO 16")
    print("-"*25)
    a16 = np.array([1,2,3,4,5])
    a16 = np.where(a16%2==0,a16+5,a16-3)
    print(a16)
    print("-"*25)

def ejercicio17():
    print("EJERCICIO 17")
    print("-"*25)
    a17 = np.array([1,2,3,4,5])
    a17 = np.where(a17%2==0,a17+5,a17-3)
    print(a17)
    print("-"*25)

def ejercicio18():
    print("EJERCICIO 18")
    print("-"*25)
    a18 = np.array([1,2,3,4,5])
    a18 = np.where(a18%2==0,a18*5,a18*3)
    print(a18)
    print("-"*25)

def ejercicio19():
    print("EJERCICIO 19")
    print("-"*25)
    a19 = np.array([1,2,3,4,5])
    a19 = np.where(a19%2==0,a19+5,a19-3)
    print(a19)
    print("-"*25)

def ejercicio20():
    print("EJERCICIO 20")
    print("-"*25)
    a20 = np.array([1,2,3,4,5])
    a20 = np.where(a20%2==0,a20+5,a20-3)
    print(a20)
    print("-"*25)

def ejercicio21():
    print("EJERCICIO 21")
    print("-"*25)
    a21 = np.array([1,2,3,4,5])
    a21 = np.where(a21%2==0,a21+5,a21-3)
    print(a21)
    print("-"*25)

def ejercicio22():
    print("EJERCICIO 22")
    print("-"*25)
    a22 = np.array([1,2,3,4,5])
    a22 = np.where(a22%2==0,a22+5,a22-3)
    print(a22)
    print("-"*25)

def ejercicio23():
    print("EJERCICIO 23")
    print("-"*25)
    a23 = np.array([1,2,3,4,5])
    a23 = np.where(a23%2==0,a23+5,a23-3)
    print(a23)
    print("-"*25)

def ejercicio24():
    print("EJERCICIO 24")
    print("-"*25)
    a24 = np.array([1,2,3,4,5])
    a24 = np.where(a24%2==0,a24+5,a24-3)
    print(a24)
    print("-"*25)

def ejercicio25():
    print("EJERCICIO 25")
    print("-"*25)
    a25 = np.array([1,2,3,4,5])
    a25 = np.where(a25%2==0,a25+5,a25-3)
    print(a25)
    print("-"*25)

def ejercicio26():
    print("EJERCICIO 26")
    print("-"*25)
    a26 = np.array([1,2,3,4,5])
    a26 = np.where(a26%2==0,a26+5,a26-3)
    print(a26)
    print("-"*25)

def ejercicio27():
    print("EJERCICIO 27")
    print("-"*25)
    a27 = np.array([1,2,3,4,5])
    a27 = np.where(a27%2==0,a27+5,a27-3)
    print(a27)
    print("-"*25)

def ejercicio28():
    print("EJERCICIO 28")
    print("-"*25)
    a28 = np.array([1,2,3,4,5])
    a28 = np.where(a28%2==0,a28+5,a28-3)
    print(a28)
    print("-"*25)

def ejercicio29():
    print("EJERCICIO 29")
    print("-"*25)
    a29 = np.array([1,2,3,4,5])
    a29 = np.where(a29%2==0,a29+5,a29-3)
    print(a29)
    print("-"*25)

def ejercicio30():
    print("EJERCICIO 30")
    print("-"*25)
    a30 = np.array([1,2,3,4,5])
    a30 = np.where(a30%2==0,a30+5,a30-3)
    print(a30)
    print("-"*25)

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
