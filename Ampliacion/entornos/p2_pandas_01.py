import pandas as pd
import datetime as dt

'''
https://pandas.pydata.org/
https://pandas.pydata.org/docs/getting_started/intro_tutorials/
https://www.w3schools.com/python/pandas/default.asp
https://www.datacamp.com/es/tutorial/pandas
'''

def ejemplo1():
    #Tipo de datos similar a un array
    # Serie desde lista
    serie = pd.Series([10, 20, 30])
    print(1,type(serie),serie)

    # Serie desde diccionario
    serie_dict = pd.Series({'a': 10, 'b': 20, 'c': 30})
    print(2,type(serie_dict),serie_dict)
    
    # Tipo de datos similar a una matriz. Puede tener etiquetas para las filas o las columnas
    # DataFrame desde diccionario
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    print(3,type(df))
    print("----")
    print(df)
    print("----")
    print(df['A'])
    print(df['B'][1])
    fila = df.iloc[0]
    print(fila)
    print(fila.iloc[1])
    

def cargaryFiltrarDataset():

    # Paso 1: Cargar el archivo CSV
    df = pd.read_csv('titanic.csv') #https://www.kaggle.com/datasets/heptapod/titanic?resource=download

    # Paso 2: Seleccionar solo algunas columnas
    columnas_seleccionadas = ['Passengerid', 'Sex', 'Age', 'Survived'] 
    df_filtrado = df[columnas_seleccionadas]

    # Paso 3: Guardar el nuevo DataFrame en un archivo CSV
    df_filtrado.to_csv('titanic_filtrado.csv', index=False)  # index=False para no guardar el índice
    
def estadisticas():

    # Paso 1: Cargar el archivo CSV descargado de Kaggle
    df = pd.read_csv('titanic.csv') 
        
    print(df.describe())
    print("----------------------")
    print(df['Age'].value_counts())#Numero de individuos de cada edad
    
def filtrado():    
    df = pd.read_csv('titanic.csv') 
        
    df_filtrado = df[df['Age'] > 30]#nos quedamos con los individuos mayores de 30
    print(df_filtrado['Age'].value_counts())# mostramos para comprobar
    
def ejercicio():
    df = pd.read_csv('titanic.csv') 
    #Quedate con los pasajeros de un sexo concreto
    
    
def limpieza():
    df = pd.read_csv('titanic.csv') 
    df.dropna(inplace=True)         # Eliminar filas con valores nulos
    df.fillna(0, inplace=True)      # Reemplazar nulos por 0
    df.drop_duplicates(inplace=True) # Eliminar duplicados
    df.to_csv('titanic_limpio.csv', index=False)

print("Empezamos")

# print(pd.__version__)
# ejemplo1()
# #cargaryFiltrarDataset()
# print("*"*50)
# estadisticas()
# print("*"*50)
# filtrado()
# print("*"*50)
# ejercicio()
# print("*"*50)
# limpieza()

print("Fin")

import pandas as pd
import numpy as np

# Datos base que usaremos en casi todos los ejercicios
np.random.seed(42)

df = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Pedro', 'Laura', 'José', 'Sofía', 'Miguel', 'Elena',
               'Pablo', 'Lucía', 'Diego', 'Carmen', 'Raúl', 'Julia', 'Marcos', 'Clara', 'Andrés', 'Valeria'],
    'edad': np.random.randint(22, 60, 20),
    'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Madrid', 'Barcelona', 'Málaga', 
               'Valencia', 'Madrid', 'Sevilla', 'Barcelona', 'Madrid', 'Bilbao', 'Valencia', 
               'Málaga', 'Madrid', 'Sevilla', 'Barcelona', 'Valencia'],
    'departamento': ['IT', 'RRHH', 'IT', 'Marketing', 'IT', 'RRHH', 'Marketing', 'IT', 'RRHH', 'Marketing',
                     'IT', 'Marketing', 'RRHH', 'IT', 'Marketing', 'RRHH', 'IT', 'Marketing', 'IT', 'RRHH'],
    'salario': np.random.randint(30000, 90000, 20),
    'fecha_ingreso': pd.date_range('2018-01-01', periods=20, freq='45D'),
    'bono': np.random.randint(0, 15000, 20),
    'activo': [True, True, False, True, True, True, False, True, True, True,
               True, False, True, True, False, True, True, True, True, False]
})

# Añadimos algunos nulos para practicar
df.loc[2:4, 'salario'] = np.nan
df.loc[10:12, 'bono'] = np.nan
df.loc[5, 'ciudad'] = np.nan

'''
Ejercicios

### Preparación común (ejecuta esto al principio)

import pandas as pd
import numpy as np

# Datos base que usaremos en casi todos los ejercicios
np.random.seed(42)

df = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Pedro', 'Laura', 'José', 'Sofía', 'Miguel', 'Elena',
               'Pablo', 'Lucía', 'Diego', 'Carmen', 'Raúl', 'Julia', 'Marcos', 'Clara', 'Andrés', 'Valeria'],
    'edad': np.random.randint(22, 60, 20),
    'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Madrid', 'Barcelona', 'Málaga', 
               'Valencia', 'Madrid', 'Sevilla', 'Barcelona', 'Madrid', 'Bilbao', 'Valencia', 
               'Málaga', 'Madrid', 'Sevilla', 'Barcelona', 'Valencia'],
    'departamento': ['IT', 'RRHH', 'IT', 'Marketing', 'IT', 'RRHH', 'Marketing', 'IT', 'RRHH', 'Marketing',
                     'IT', 'Marketing', 'RRHH', 'IT', 'Marketing', 'RRHH', 'IT', 'Marketing', 'IT', 'RRHH'],
    'salario': np.random.randint(30000, 90000, 20),
    'fecha_ingreso': pd.date_range('2018-01-01', periods=20, freq='45D'),
    'bono': np.random.randint(0, 15000, 20),
    'activo': [True, True, False, True, True, True, False, True, True, True,
               True, False, True, True, False, True, True, True, True, False]
})

# Añadimos algunos nulos para practicar
df.loc[2:4, 'salario'] = np.nan
df.loc[10:12, 'bono'] = np.nan
df.loc[5, 'ciudad'] = np.nan
*****

'''

def ejercicio1():

    # 1. Muestra las primeras 8 filas y las últimas 5 filas del DataFrame.
    print("8 primeras lineas\n\n\n", df.head(8))
    print("5 ultimas lineas\n\n\n", df.tail(5))

ejercicio1()

def ejercicio2():
    print("Ejercicio 2\n\n\n")
    print(df.shape) #Muestra las filas y columnas del DataFrame
    print("Numero de filas\n", df.shape[0])
    print("Numero de columnas\n", df.shape[1])

ejercicio2()

def ejercicio3():
    print("Ejercicio 3\n\n\n")
    print(df.columns)

ejercicio3()

def ejercicio4():
    print("Ejercicio 4\n\n\n")
    print(df.isnull().sum())

ejercicio4()

def ejercicio5():
    print("Ejercicio 5\n\n\n")
    print(df["nombre"]) # Objeto unidimensional
    print(df[["nombre"]]) # Objeto bidimensional

ejercicio5()

def ejercicio6():
    print("Ejercicio 6\n\n\n")
    print(df[["nombre", "edad", "salario"]]) # Como dataframe

ejercicio6()

def ejercicio7():

    print("Ejercicio 7\n\n\n")
    print(df.iloc[5:13]) #Primer indice inclusivo, segundo exclusivo

ejercicio7()

def ejercicio8():

    print("Ejercicio 8\n\n\n")

    print(df.loc[[0,5,10,15]])

ejercicio8()

def ejercicio9():

    print("Ejercicio 9\n\n\n")

    print(df[df["edad"] > 45])

ejercicio9()

def ejercicio10():

    print("Ejercicio 10\n\n\n")

    print(df[(df["ciudad"] == "Madrid") & (df["activo"] == True)])

ejercicio10()

def ejercicio11():

    # 11. Filtra los empleados cuyo nombre empiece por 'A' o 'M'.

    print("\n\n\nEjercicio 11")

    print(df[df["nombre"].str.startswith("A") | df["nombre"].str.startswith("M")])

ejercicio11()

def ejercicio12():

    # 12. Crea una nueva columna `salario_anual` que sea el salario × 14 (12 meses + 2 pagas extra).

    print("\n\n\nEjercicio 11")

    # Dos opciones para manejar los nulos, borrar esos registros o rellenarlos con 0

    # df.dropna(subset=["salario"], inplace=True)
    # df["salario_anual"] = df["salario_anual"].fillna(0)

    df["salario_anual"] = df["salario"] * 14 # Los empleados en los indices 3,4,2, tienen NaN en su salario

    print(df["salario_anual"])

ejercicio12()

def ejercicio13():

    # 13. Crea una columna `antiguedad_años` redondeada (hoy - fecha_ingreso).

    print("\n\n\nEjercicio 13")

    fechas = pd.to_datetime(df["fecha_ingreso"])

    diferencia = dt.datetime.now() - fechas

    df["antiguedad_anios"] = (diferencia.dt.days / 365.25).round(0).astype(int)

    print(df["fecha_ingreso"])

    print(df["antiguedad_anios"])


ejercicio13()

def ejercicio14():

    '''14. Crea una columna `categoria_edad` que sea:  
    - "Joven" (< 30), "Adulto" (30-45), "Senior" (> 45)'''

    df["categoria_edad"] = pd.cut(

        df["edad"],
        bins=[0,29,45, float("inf")],
        labels=["Joven", "Adulto", "Senior"]
    )

    print(df[['edad', 'categoria_edad']])


ejercicio14()

def ejercicio15():

    # 15. Aumenta un 10% el salario a todos los empleados del departamento IT.

    print(df[["salario", "departamento"]])

    salarios_it = df["salario"][df["departamento"] == "IT" ]
    # print(salarios_it)

    salarios_it *= 1.1

    # print(salarios_it)

    # df["salario"][df["departamento"] == "IT"] = salarios_it
    df.loc[df["departamento"] == "IT", "salario"] = salarios_it # Con loc evitamos problemas de copias

    print(df[["salario", "departamento"]])

    # print(df["salario"])
    # df["salario"] = df[df["departamento"] == "IT"] * 1.10

    # print(df["salario"])

ejercicio15()

def ejercicio16():

    # 16. Rellena los salarios nulos con la media del salario por departamento.

    # Calculamos la media por departamento y la asignamos a cada fila correspondiente
    df["salario"] = df["salario"].fillna(df.groupby("departamento")["salario"].transform("mean"))
    
    # Una vez corregido el salario, recalculamos o rellenamos el salario_anual
    df["salario_anual"] = df["salario_anual"].fillna(df["salario"] * 14)

    print(df[["nombre", "departamento", "salario"]])

ejercicio16()

def ejercicio17():

    # 17. Elimina todas las filas donde `bono` sea nulo.

    df.dropna(subset=["bono"], inplace=True)

    print(df["bono"])

ejercicio17()

def ejercicio18():

    # 18. Ordena el DataFrame por salario de forma descendente.

    print(df.sort_values(by=["salario"], ascending=False))

ejercicio18()

def ejercicio19():

    # 19. Ordena primero por ciudad (asc) y luego por salario (desc).

    print(df.sort_values(by=["ciudad", "salario"], ascending=[True, False]))

def ejercicio20():

    # 20. ¿Cuál es el salario medio, máximo y mínimo por departamento?

    print("Salario máximo de cada columna\n", df.groupby("departamento")["salario"].max())
    print("Salario medio de cada columna\n", df.groupby("departamento")["salario"].mean())
    print("Salario minimo de cada columna\n", df.groupby("departamento")["salario"].min())

ejercicio20()

def ejercicio21():

    # 21. ¿Cuántos empleados hay por ciudad? Muestra también el salario medio.

    print("Empleados por ciudad", df.groupby("ciudad")["ciudad"].count())
    print("El salario medio de cada ciudad es: ", np.round(df.groupby("ciudad")["salario"].mean(), 2))

ejercicio21()

def ejercicio22():

    # Calcula el salario total (salario + bono) y llámalo `compensacion_total`.  
    # Luego ordena de mayor a menor compensación.

    df["compensacion_total"] = df["salario"] + df["bono"]

    print(df.sort_values(by="compensacion_total", ascending=False))

ejercicio22()

def ejercicio23():

    # 23. Usando `groupby`, encuentra el empleado con mayor salario de cada departamento (nombre y salario).
    index = df.groupby("departamento")["salario"].idxmax()
    print(df.loc[index, ["departamento", "nombre", "salario"]])

ejercicio23()

def ejercicio24():

    # 24. Crea una tabla pivot que muestre el salario medio por departamento (filas) y ciudad (columnas).

    print("\n\n\n\n\n\n")

    pivot_df = df.pivot_table(

        index="departamento", # Registros
        columns="ciudad", # Atritutos
        values="salario", ## Valor de los registros
        aggfunc="mean" ## Funcion de agrupación de los datos

    )

    print(pivot_df)


ejercicio24()

def ejercicio25():

    # 25. Une este DataFrame con el siguiente (simula una tabla de objetivos):

    global df

    objetivos = pd.DataFrame({
        'departamento': ['IT', 'RRHH', 'Marketing'],
        'objetivo_ventas': [500000, 200000, 800000]
    })

    df = df.merge(objetivos, on="departamento", how="left") ## Similar a realizar un left join en sql. Es decir añadir las filas de la derecha que aparecen a la izquierda

    print(df.groupby("departamento")["objetivo_ventas"].min())

ejercicio25()

def ejercicio26():

    '''
    
    26. Con los datos unidos, crea una columna `cumple_objetivo` 
    que sea True si el departamento tiene objetivo y el salario > 60000 (simulación simple).
    
    '''
    # Segun la media del salario del departamento

    media_salarios = df.groupby("departamento")["salario"].transform("mean")

    print(media_salarios)

    df["cumple_objetivo"] = (df["objetivo_ventas"].notna()) & (media_salarios > 60000)

    print(df[["nombre","departamento","salario","objetivo_ventas","cumple_objetivo"]])

    # Segun la suma de los salarios del departamento

    # suma_salarios = df.groupby("departamento")["salario"].transform("sum")

    # print(suma_salarios)

    # df["cumple_objetivo"] = (df["objetivo_ventas"].notna()) & (suma_salarios > 60000)

    # print(df[["nombre","departamento","salario","objetivo_ventas","cumple_objetivo"]])

ejercicio26()

def ejercicio27():

    # 27. Guarda el DataFrame final en CSV y en Excel (dos archivos distintos).
 
    df.to_excel("dataframe.xlsx", sheet_name="Dataframe", index=False, float_format="%.2f") # Necesaria la libreria openpyxl para exportarlo a xlsx
    df.to_csv("dataframe.csv", ";", index=False, float_format="%.2f")

ejercicio27()

# print("Dataframe original\n", df)

def ejercicio28():

    # 28. Lee de nuevo el CSV que acabas de guardar y comprueba que todo está igual.

    df = pd.read_csv("dataframe.csv")

    print("Dataframe nuevo \n", df)

ejercicio28()

def ejercicio29():

    '''
    Docstring for ejercicio29
    
    29. Trabaja con fechas:  
    - Extrae el año y el mes de `fecha_ingreso` en columnas nuevas.  
    - Filtra los empleados que entraron en 2020 o después.

    '''

    df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"])

    df["anio_ingreso"] = df["fecha_ingreso"].dt.year
    df["mes_ingreso"] = df["fecha_ingreso"].dt.month

    df_filtrado = df[df["anio_ingreso"] >= 2020]

    print(df_filtrado)

    # print(df["anio_ingreso"])

ejercicio29()

def ejercicio30(df : pd.DataFrame):

    '''
    Docstring for ejercicio30
    
    30. (Reto final) Crea una función que reciba un DataFrame y devuelva un resumen con:
    - Número total de empleados
    - Salario medio y mediana
    - Departamento con mayor salario medio
    - Porcentaje de empleados activos
    - Ciudad con más empleados

    '''

    media_salarios = df.groupby("departamento")["salario"].mean() ## Devuelve la media de los salarios por departamento
    departamento_max_salario = media_salarios.idxmax() ## Devuelve el indice del departamento con el salario medio mas alto

    total_empleados = df["nombre"].count()

    # empleados_activos = df[df["activo"] == True]["nombre"].count()
    empleados_activos = df["activo"].sum() # Si es true suma 1 si es false suma 0

    empleados_ciudad = df.groupby("ciudad")["nombre"].count()

    ciudad_max_empleados = empleados_ciudad.idxmax()

    porcentaje_activos = np.round((empleados_activos / total_empleados) * 100, 2)

    print("Numero de empleados totales: ", total_empleados)
    print("Salario medio de la empresa", np.round(df["salario"].mean(), 2))
    print("Mediana del salario de la empresa", np.round(df["salario"].median(), 2))
    print("Departamento con el mayor salario medio", departamento_max_salario)
    print("Procentaje de empleados activos", porcentaje_activos, "%")
    print("La ciudad con mas empleados es: ", ciudad_max_empleados)

ejercicio30(df)

'''

### Ejercicios

1. Muestra las primeras 8 filas y las últimas 5 filas del DataFrame.

2. ¿Cuántas filas y columnas tiene el DataFrame?

3. Muestra solo los nombres de las columnas y sus tipos de datos.

4. ¿Cuántos valores nulos hay en cada columna?

5. Selecciona solo la columna `nombre` como Series y como DataFrame.

6. Selecciona las columnas `nombre`, `edad` y `salario`.

7. Muestra las filas de la posición 5 a la 12 (inclusive) usando `iloc`.

8. Muestra las filas con índice 0, 5, 10 y 15 usando `loc`.

9. Filtra los empleados que tienen más de 45 años.

10. Filtra los empleados de Madrid que estén activos.

11. Filtra los empleados cuyo nombre empiece por 'A' o 'M'.

12. Crea una nueva columna `salario_anual` que sea el salario × 14 (12 meses + 2 pagas extra).

13. Crea una columna `antiguedad_años` redondeada (hoy - fecha_ingreso).

14. Crea una columna `categoria_edad` que sea:  
    - "Joven" (< 30), "Adulto" (30-45), "Senior" (> 45)

15. Aumenta un 10% el salario a todos los empleados del departamento IT.

16. Rellena los salarios nulos con la media del salario por departamento.

17. Elimina todas las filas donde `bono` sea nulo.

18. Ordena el DataFrame por salario de forma descendente.

19. Ordena primero por ciudad (asc) y luego por salario (desc).

20. ¿Cuál es el salario medio, máximo y mínimo por departamento?

21. ¿Cuántos empleados hay por ciudad? Muestra también el salario medio.

22. Calcula el salario total (salario + bono) y llámalo `compensacion_total`.  
    Luego ordena de mayor a menor compensación.

23. Usando `groupby`, encuentra el empleado con mayor salario de cada departamento (nombre y salario).

24. Crea una tabla pivot que muestre el salario medio por departamento (filas) y ciudad (columnas).

25. Une este DataFrame con el siguiente (simula una tabla de objetivos):

```python
objetivos = pd.DataFrame({
    'departamento': ['IT', 'RRHH', 'Marketing'],
    'objetivo_ventas': [500000, 200000, 800000]
})
```
Haz un merge para añadir el objetivo a cada empleado.

26. Con los datos unidos, crea una columna `cumple_objetivo` que sea True si el departamento tiene objetivo y el salario > 60000 (simulación simple).

27. Guarda el DataFrame final en CSV y en Excel (dos archivos distintos).

28. Lee de nuevo el CSV que acabas de guardar y comprueba que todo está igual.

29. Trabaja con fechas:  
    - Extrae el año y el mes de `fecha_ingreso` en columnas nuevas.  
    - Filtra los empleados que entraron en 2020 o después.

30. (Reto final) Crea una función que reciba un DataFrame y devuelva un resumen con:
    - Número total de empleados
    - Salario medio y mediana
    - Departamento con mayor salario medio
    - Porcentaje de empleados activos
    - Ciudad con más empleados


'''
