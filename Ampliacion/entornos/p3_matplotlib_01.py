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

# ejercicio15()
# ejercicio16()
# ejercicio17()
# ejercicio18()
# ejercicio19()
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
