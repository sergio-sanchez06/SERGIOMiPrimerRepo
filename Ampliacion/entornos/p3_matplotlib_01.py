'''
https://matplotlib.org/
https://matplotlib.org/stable/tutorials/index
https://www.w3schools.com/python/matplotlib_intro.asp
https://www.datacamp.com/es/tutorial/matplotlib-tutorial-python
https://www.geeksforgeeks.org/python/matplotlib-tutorial/

'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def ejemplo1():
    #Grafico de lineas
    x = [1, 2, 3, 4]
    y = [1, 4, 2, 3]
    plt.plot(x, y)
    plt.show()
    
def ejemplo2():
    #Grafico de barras
    x = ['A', 'B', 'C']
    y = [5, 3, 7]
    plt.bar(x, y)
    plt.show()
    
def ejemplo3():
    #Grafico de barras horizontales
    x = ['A', 'B', 'C']
    y = [5, 3, 7]
    plt.barh(x, y)
    plt.show()
    
def ejemplo4():
    #Grafico de dispersion
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    plt.scatter(x, y)
    plt.show()   
    
def ejemplo5():
    import numpy as np
    data = np.random.randn(1000)
    plt.hist(data, bins=30)
    plt.show()
    
def ejemplo6():
    import numpy as np
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    plt.hist2d(x, y, bins=30)
    plt.colorbar()
    plt.title('Histograma 2D')
    plt.show()
    
# def ejercicios():
#     #Mostrar el histograma de la edad de los pasajeros del titanic
    
#     #Mostrar el histograma de la edad de los pasajeros del titanic menores de 50



print("Empezamos")

#ejemplo1()
print("*"*50)
#ejemplo2()
print("*"*50)
#ejemplo3()
print("*"*50)
#ejemplo4()
print("*"*50)
#ejemplo5()
print("*"*50)
#ejemplo6()
print("*"*50)
# ejercicios()

def ejercicio1():
    print("Ejercicio 1: Línea simple con etiquetas")
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 2, 3, 5]
    plt.plot(x, y)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico de Línea Simple')
    plt.show()

def ejercicio2():
    print("Ejercicio 2: Dos líneas (x² y x³)")
    x = np.linspace(0, 10, 50)
    plt.plot(x, x**2, label='x²', color='blue')
    plt.plot(x, x**3, label='x³', color='green')
    plt.legend()
    plt.title('Comparación de Potencias')
    plt.show()

def ejercicio3():
    print("Ejercicio 3: Seno y Coseno con Grid")
    x = np.linspace(0, 2 * np.pi, 100)
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

def ejercicio4():
    print("Ejercicio 4: Dispersión aleatoria")
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.scatter(x, y, alpha=0.5, c='purple')
    plt.title('Scatter Plot Aleatorio')
    plt.show()

def ejercicio5():
    print("Ejercicio 5: Barras de colores")
    cats = ["A", "B", "C", "D", "E"]
    vals = [10, 24, 15, 30, 12]
    colores = ['red', 'blue', 'green', 'orange', 'cyan']
    plt.bar(cats, vals, color=colores)
    plt.title('Gráfico de Barras')
    plt.show()

def ejercicio6():
    print("Ejercicio 6: Histograma normal")
    data = np.random.normal(0, 1, 1000)
    plt.hist(data, bins=30, edgecolor='black', color='skyblue')
    plt.title('Distribución Normal')
    plt.show()

def ejercicio7():
    print("Ejercicio 7: Pie chart explotado")
    proporciones = [20, 30, 25, 25]
    etiquetas = ["Grupo A", "Grupo B", "Grupo C", "Grupo D"]
    explota = (0, 0.1, 0, 0) # Explota el Grupo B
    plt.pie(proporciones, labels=etiquetas, explode=explota, autopct='%1.1f%%')
    plt.title('Proporciones por Grupo')
    plt.show()

def ejercicio8():
    print("Ejercicio 8: Subplots 2x2")
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    
    # Línea
    axs[0, 0].plot([1, 2, 3], [1, 2, 3])
    axs[0, 0].set_title('Línea')
    
    # Barras
    axs[0, 1].bar(['X', 'Y'], [5, 10])
    axs[0, 1].set_title('Barras')
    
    # Dispersión
    axs[1, 0].scatter(np.random.rand(10), np.random.rand(10))
    axs[1, 0].set_title('Dispersión')
    
    # Histograma
    axs[1, 1].hist(np.random.randn(100))
    axs[1, 1].set_title('Histograma')
    
    plt.tight_layout()
    plt.show()

def ejercicio9():
    print("Ejercicio 9: Marcadores y línea punteada")
    x = np.arange(10)
    y = x * 2
    plt.plot(x, y, 'ro--', label='Datos') # r=rojo, o=círculo, --=punteado
    plt.legend()
    plt.show()

def ejercicio10():
    print("Ejercicio 10: Barras apiladas")
    labels = ['G1', 'G2', 'G3']
    serie1 = [10, 20, 15]
    serie2 = [5, 15, 10]
    plt.bar(labels, serie1, label='Serie 1')
    plt.bar(labels, serie2, bottom=serie1, label='Serie 2')
    plt.legend()
    plt.show()

def ejercicio11():
    print("Ejercicio 11: Gráfico de áreas apiladas")
    x = range(1, 6)
    y = [ [1, 4, 6, 8, 9], [2, 2, 7, 10, 12], [2, 8, 5, 10, 6] ]
    plt.stackplot(x, y, labels=['A', 'B', 'C'])
    plt.legend(loc='upper left')
    plt.show()

def ejercicio12():
    print("Ejercicio 12: Boxplot")
    datos = [np.random.normal(0, std, 100) for std in range(1, 4)]
    plt.boxplot(datos, patch_artist=True)
    plt.title('Boxplot de Varias Distribuciones')
    plt.show()

def ejercicio13():
    print("Ejercicio 13: Gráfico de contorno")
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) + np.cos(Y)
    cp = plt.contourf(X, Y, Z)
    plt.colorbar(cp)
    plt.title('Contorno: sin(x) + cos(y)')
    plt.show()

def ejercicio14():
    print("Ejercicio 14: Violin Plot")
    datos = [np.random.normal(0, std, 100) for std in range(1, 4)]
    plt.violinplot(datos)
    plt.title('Violin Plot')
    plt.show()


def ejercicio15():

    '''
    15. Agrega anotaciones (annotations) a un gráfico de línea, marcando el punto máximo con texto y una flecha.

    '''

    x = [1, 2, 3, 4, 5]
    y = [1, 4, 2, 3, 5]
    plt.plot(x, y)
    plt.annotate('Punto máximo', xy=(5, 5), xytext=(6, 6), arrowprops=dict(facecolor='red', shrink=0.05))
    plt.show()

def ejercicio16():
    
    # 16. Crea un gráfico polar con una espiral o una rosa polar.
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    
    t = np.linspace(0, 2 * np.pi, 100)
    r = np.sin(4 * t)
    
    ax.plot(t, r)

    ax.set_rticks([])
    ax.set_rlabel_position(-22.5)
    ax.grid(True)

    plt.show()

def ejercicio17():

    # 17. Usa estilos predefinidos de Matplotlib (como 'ggplot' o 'seaborn') y compara dos gráficos con diferentes estilos.
    
    plt.style.use('ggplot')
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
    
    plt.style.use('seaborn-v0_8')
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

def ejercicio18():
    
    # 18. Grafica datos de un DataFrame de Pandas (crea uno simple) usando el método .plot().
    
    columna_x = np.linspace(0, 10, 100)
    columna_y = np.sin(columna_x)

    df = pd.DataFrame({
        'x': columna_x,
        'y': columna_y
    })
    df.plot(x='x', y='y')
    plt.show()

def ejercicio19():
    
    # 19. Crea un gráfico 3D de líneas o superficie usando axes3d.
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)
    
    ax.plot(x, y, z)
    plt.show()

def ejercicio20():
    
    # 20. Guarda un gráfico en diferentes formatos (PNG, PDF, SVG) y ajusta parámetros como dpi y tamaño de figura.

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)
    
    ax.plot(x, y, z)

    plt.savefig('grafico_3d.png', dpi=100)
    plt.savefig('grafico_3d.pdf', dpi=100)
    plt.savefig('grafico_3d.svg', dpi=100)

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

print("Fin")

'''pip install
Puedes usar datos simples (listas o arrays de NumPy) para resolverlos. ¡Intenta implementarlos tú mismo antes de buscar soluciones!

1. Crea un gráfico de línea simple con los puntos x = [1, 2, 3, 4, 5] e y = [1, 4, 2, 3, 5]. Agrega etiquetas a los ejes y un título.

2. Dibuja dos líneas en el mismo gráfico: una con y = x² y otra con y = x³, para x de 0 a 10. Usa diferentes colores y agrega una leyenda.

3. Grafica la función seno (sin(x)) y coseno (cos(x)) en el rango de 0 a 2π. Usa una cuadrícula (grid).

4. Crea un gráfico de dispersión (scatter) con 100 puntos aleatorios generados con NumPy.

5. Dibuja un gráfico de barras con categorías ["A", "B", "C", "D", "E"] y valores [10, 24, 15, 30, 12]. Agrega colores diferentes a cada barra.

6. Crea un histograma con 1000 valores aleatorios de una distribución normal (media 0, desviación 1).

7. Dibuja un gráfico circular (pie chart) que muestre la proporción de [20, 30, 25, 25] con etiquetas ["Grupo A", "Grupo B", "Grupo C", "Grupo D"] y explota una porción.

8. Usa subplots para mostrar 4 gráficos en una figura: línea, barras, dispersión e histograma (en una cuadrícula 2x2).

9. Grafica una línea con marcadores personalizados (por ejemplo, círculos rojos) y línea punteada.

10. Crea un gráfico de barras apiladas (stacked bar) con dos series de datos.

11. Dibuja un gráfico de áreas (area plot) con varias series apiladas.

12. Grafica un boxplot con varios conjuntos de datos aleatorios.

13. Crea un gráfico de contorno (contour plot) de la función z = sin(x) + cos(y) en una malla.

14. Dibuja un gráfico de violín (violin plot) comparando varias distribuciones aleatorias.

15. Agrega anotaciones (annotations) a un gráfico de línea, marcando el punto máximo con texto y una flecha.

16. Crea un gráfico polar con una espiral o una rosa polar.

17. Usa estilos predefinidos de Matplotlib (como 'ggplot' o 'seaborn') y compara dos gráficos con diferentes estilos.

18. Grafica datos de un DataFrame de Pandas (crea uno simple) usando el método .plot().

19. Crea un gráfico 3D de líneas o superficie usando axes3d.

20. Guarda un gráfico en diferentes formatos (PNG, PDF, SVG) y ajusta parámetros como dpi y tamaño de figura.

'''
