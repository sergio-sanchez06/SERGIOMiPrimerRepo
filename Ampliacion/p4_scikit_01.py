'''
https://scikit-learn.org/stable/
https://www.datacamp.com/es/tutorial/machine-learning-python
https://www.digitalocean.com/community/tutorials/python-scikit-learn-tutorial
https://www.geeksforgeeks.org/machine-learning/scikit-learn-tutorial/
https://scikit-learn.org/1.4/tutorial/index.html
https://www.tutorialspoint.com/scikit_learn/index.htm

'''
def ejem01():
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score

    # Cargar el dataset iris
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Dividir en conjunto de entrenamiento y prueba 80/20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el clasificador de árbol de decisión
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = clf.predict(X_test)

    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')

    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')


#Evaluacion con crossvalidation    
def ejem02():
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import cross_val_score
    from sklearn.metrics import make_scorer, precision_score, recall_score

    # Cargar el dataset iris
    iris = load_iris()
    X, y = iris.data, iris.target

    # Crear el clasificador
    clf = DecisionTreeClassifier(random_state=42)

    # Definir los scorers para precisión y recall promediados (macro para multiclase)
    precision = make_scorer(precision_score, average='macro')
    recall = make_scorer(recall_score, average='macro')

    # Calcular accuracy, precision y recall usando 10-fold cross validation
    accuracy_scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
    precision_scores = cross_val_score(clf, X, y, cv=10, scoring=precision)
    recall_scores = cross_val_score(clf, X, y, cv=10, scoring=recall)

    # Mostrar resultados promedio
    print(f'Accuracy promedio: {accuracy_scores.mean():.2f}')
    print(f'Precision promedio: {precision_scores.mean():.2f}')
    print(f'Recall promedio: {recall_scores.mean():.2f}')
   
#Evaluacion con crossvalidation calculada por el programa
def ejem03():
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
    import numpy as np
    import matplotlib.pyplot as plt

    # Cargar el dataset iris
    iris = load_iris()
    X, y = iris.data, iris.target

    # Inicializar el clasificador y la validación cruzada
    clf = DecisionTreeClassifier(random_state=42)
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

    # Listas para almacenar resultados
    accuracies = []
    precisions = []
    recalls = []
    conf_matrix_total = np.zeros((len(np.unique(y)), len(np.unique(y))), dtype=int)

    # Cross-validation manual para poder acumular la matriz de confusión
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracies.append(accuracy_score(y_test, y_pred))
        precisions.append(precision_score(y_test, y_pred, average='macro'))
        recalls.append(recall_score(y_test, y_pred, average='macro'))
        conf_matrix_total += confusion_matrix(y_test, y_pred, labels=np.unique(y))

    # Mostrar métricas promedio
    print(f'Accuracy promedio: {np.mean(accuracies):.2f}')
    print(f'Precision promedio: {np.mean(precisions):.2f}')
    print(f'Recall promedio: {np.mean(recalls):.2f}')

    # Mostrar la matriz de confusión acumulada
    print("\nMatriz de confusión acumulada (10 folds):")
    print(conf_matrix_total)

    # Visualizar la matriz de confusión
    disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_total, display_labels=iris.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Matriz de confusión acumulada (10 folds)")
    plt.show()
    
def ejer():
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    
    from sklearn.model_selection import cross_val_score
    from sklearn.metrics import make_scorer, precision_score, recall_score
    from sklearn import svm

    # Cargar el dataset iris
    iris = load_iris()
    X, y = iris.data, iris.target

    print("PART")
    # Crear el clasificador
    clf = DecisionTreeClassifier(random_state=42)

    # Definir los scorers para precisión y recall promediados (macro para multiclase)
    precision = make_scorer(precision_score, average='macro')
    recall = make_scorer(recall_score, average='macro')

    # Calcular accuracy, precision y recall usando 10-fold cross validation
    accuracy_scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
    precision_scores = cross_val_score(clf, X, y, cv=10, scoring=precision)
    recall_scores = cross_val_score(clf, X, y, cv=10, scoring=recall)

    # Mostrar resultados promedio
    print(f'Accuracy promedio: {accuracy_scores.mean():.2f}')
    print(f'Precision promedio: {precision_scores.mean():.2f}')
    print(f'Recall promedio: {recall_scores.mean():.2f}')
    
    #COMPLETAR CON DOS ALGORITMOS MAS
    



    
print("Empezamos")
#ejemplo1()
#ejem01()
print("---------")
#ejem02()
print("---------")
#ejem03()
print("---------")
ejer()
print("---------")

def ejercicio1():

    from sklearn import datasets
    from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
    from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
    from sklearn.linear_model import LogisticRegression, LinearRegression

    # Cargar el dataset iris
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Dividir en conjunto de entrenamiento y prueba 80/20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el clasificador de árbol de decisión
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = clf.predict(X_test)

    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')

    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')

ejercicio1()

def ejercicio2():

    # Carga el dataset Digits (imágenes de números). Prueba KNN, SVM y Random Forest. Compara sus precisiones con train_test_split y accuracy_score.
    
    from sklearn import datasets
    
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target

    # Dividir en conjunto de entrenamiento y prueba 80/20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el clasificador de árbol de decisión
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = clf.predict(X_test)

    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')

    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')

ejercicio2()

def ejercicio3():

    # Carga el dataset Diabetes (regresión). Usa LinearRegression y calcula el MSE con cross_val_score (5 folds).
    
    from sklearn import datasets
    
    diabetes = datasets.load_diabetes()
    X = diabetes.data
    y = diabetes.target

    # Dividir en conjunto de entrenamiento y prueba 80/20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el clasificador de árbol de decisión
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = clf.predict(X_test)

    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')

    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')

ejercicio3()

def ejercicio4():

    # Entrena un DecisionTreeClassifier en Iris. Visualiza el árbol (usa plot_tree si tienes Graphviz) y evalúa la precisión.
    
    from sklearn import datasets
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    
    # Cargar el dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    
    # Dividir en conjunto de entrenamiento y prueba 80/20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Crear y entrenar el clasificador de árbol de decisión
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    
    # Realizar predicciones
    y_pred = clf.predict(X_test)
    
    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    
    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    
    # Visualizar el árbol
    plot_tree(clf)
    plt.show()  

ejercicio4()

def ejercicio5():

    # Usa SVC en el dataset Iris. Busca los mejores parámetros (C y kernel) con GridSearchCV y muestra el mejor score.

    from sklearn.datasets import load_iris
    from sklearn.model_selection import GridSearchCV, train_test_split
    from sklearn.svm import SVC

    # 1. Cargar datos
    iris = load_iris()
    X, y = iris.data, iris.target

    # 2. Definir el espacio de búsqueda (parámetros a probar)
    # C: Parámetro de regularización
    # kernel: Tipo de función de base para la frontera de decisión
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'gamma': ['scale', 'auto']  # Opcional, pero influye mucho en rbf
    }

    # 3. Configurar GridSearchCV
    # cv=5 significa validación cruzada de 5 pliegues
    grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')

    # 4. Entrenar con la búsqueda de malla
    grid_search.fit(X, y)

    # 5. Resultados
    print(f"Mejores parámetros encontrados: {grid_search.best_params_}")
    print(f"Mejor score (exactitud): {grid_search.best_score_:.4f}")

ejercicio5()

def ejercicio6():

    # Carga Iris (solo características, sin etiquetas). Aplica KMeans con 3 clusters. Compara los clusters predichos con las etiquetas reales.

    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    from sklearn.cluster import KMeans
    import pandas as pd

    # 1. Cargar el dataset
    iris = load_iris()
    X = iris.data  # Solo características (longitud/ancho de sépalo y pétalo)
    y_real = iris.target  # Etiquetas reales para la comparación final

    # 2. Aplicar KMeans con 3 clusters
    # Definimos random_state para que los resultados sean reproducibles
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    y_kmeans = kmeans.fit_predict(X)

    # 3. Comparación visual
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Gráfico de las etiquetas reales
    ax1.scatter(X[:, 2], X[:, 3], c=y_real, cmap='viridis')
    ax1.set_title('Etiquetas Reales (Especies)')
    ax1.set_xlabel('Longitud del pétalo')
    ax1.set_ylabel('Ancho del pétalo')

    # Gráfico de los clusters de KMeans
    ax2.scatter(X[:, 2], X[:, 3], c=y_kmeans, cmap='plasma')
    ax2.set_title('Clusters Predichos (K-Means)')
    ax2.set_xlabel('Longitud del pétalo')
    ax2.set_ylabel('Ancho del pétalo')

    plt.show()

    # 4. Tabla de contingencia para ver la precisión
    df_comparacion = pd.DataFrame({'Real': y_real, 'KMeans': y_kmeans})
    print("Tabla de contingencia (Cruce de etiquetas):")
    print(pd.crosstab(df_comparacion['Real'], df_comparacion['KMeans']))

ejercicio6()

def ejercicio7():

    # Aplica PCA al dataset Digits para reducir a 2 componentes. Visualiza los datos en un scatter plot coloreado por clase.

    import matplotlib.pyplot as plt
    from sklearn.datasets import load_digits
    from sklearn.decomposition import PCA
    import pandas as pd

    # 1. Cargar el dataset
    digits = load_digits()
    X = digits.data
    y = digits.target

    # 2. Aplicar PCA para reducir a 2 componentes
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # 3. Visualización
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', alpha=0.7, edgecolors='none')

    # Añadir detalles al gráfico
    plt.colorbar(scatter, label='Dígito (Clase)')
    plt.title('PCA del Dataset Digits (Reducción a 2D)')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

ejercicio7()

def ejercicio8():

    # Entrena un RandomForestClassifier en Iris o Breast Cancer (datasets.load_breast_cancer()). Muestra la importancia de las características con feature_importances_.
    
    from sklearn import datasets
    from sklearn.ensemble import RandomForestClassifier
    import matplotlib.pyplot as plt
    
    # Cargar el dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    
    # Entrenar el modelo
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X, y)
    
    # Mostrar importancia de características
    importances = clf.feature_importances_
    
    # Visualizar
    plt.figure(figsize=(10, 6))
    plt.barh(iris.feature_names, importances)
    plt.xlabel('Importancia')
    plt.title('Importancia de las características')
    plt.show()

ejercicio8()

def ejercicio9():

    # Crea un Pipeline con StandardScaler y LogisticRegression. Aplícalo al dataset Wine (datasets.load_wine()) y evalúa con cross_val_score.

    from sklearn import datasets
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score
    
    # Cargar el dataset
    wine = datasets.load_wine()
    X = wine.data
    y = wine.target
    
    # Crear el pipeline
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression())
    ])
    
    # Evaluar con cross_val_score
    scores = cross_val_score(pipe, X, y, cv=5)
    
    # Imprimir resultados
    print(f"Scores: {scores}")
    print(f"Media de scores: {scores.mean()}")

ejercicio9()

def ejercicio10():

    # Usa el dataset Boston (o California Housing en versiones nuevas: fetch_california_housing). Compara LinearRegression con RandomForestRegressor en términos de MSE.

    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    
    # Cargar el dataset
    boston = datasets.load_boston()
    X = boston.data
    y = boston.target
    
    # Dividir en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenar modelos
    lr = LinearRegression()
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    
    lr.fit(X_train, y_train)
    rf.fit(X_train, y_train)
    
    # Predecir
    y_pred_lr = lr.predict(X_test)
    y_pred_rf = rf.predict(X_test)
    
    # Calcular MSE
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    
    print(f"MSE LinearRegression: {mse_lr}")
    print(f"MSE RandomForestRegressor: {mse_rf}")

ejercicio10()

print("Fin")

'''
Aquí tienes **10 ejercicios prácticos** para practicar con **scikit-learn**. Todos usan conjuntos de datos incluidos en la biblioteca (como Iris, Digits o Diabetes), para que puedas empezar rápidamente sin descargar nada extra.

Importa lo necesario al inicio:

"""python
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
"""

### 1. Clasificación básica con Iris
Carga el dataset Iris. Divide en train/test (80/20). Entrena una regresión logística y calcula la precisión.

### 2. Comparación de clasificadores en Digits
Carga el dataset Digits (imágenes de números). Prueba KNN, SVM y Random Forest. Compara sus precisiones con train_test_split y accuracy_score.

### 3. Validación cruzada en Diabetes
Carga el dataset Diabetes (regresión). Usa LinearRegression y calcula el MSE con cross_val_score (5 folds).

### 4. Árbol de decisión en Iris
Entrena un DecisionTreeClassifier en Iris. Visualiza el árbol (usa plot_tree si tienes Graphviz) y evalúa la precisión.

### 5. Ajuste de hiperparámetros con GridSearchCV
Usa SVC en el dataset Iris. Busca los mejores parámetros (C y kernel) con GridSearchCV y muestra el mejor score.

### 6. Clustering con KMeans
Carga Iris (solo características, sin etiquetas). Aplica KMeans con 3 clusters. Compara los clusters predichos con las etiquetas reales.

### 7. Reducción de dimensionalidad con PCA
Aplica PCA al dataset Digits para reducir a 2 componentes. Visualiza los datos en un scatter plot coloreado por clase.

### 8. Random Forest y importancia de características
Entrena un RandomForestClassifier en Iris o Breast Cancer (datasets.load_breast_cancer()). Muestra la importancia de las características con feature_importances_.

### 9. Pipeline completo
Crea un Pipeline con StandardScaler y LogisticRegression. Aplícalo al dataset Wine (datasets.load_wine()) y evalúa con cross_val_score.

### 10. Regresión con ensemble
Usa el dataset Boston (o California Housing en versiones nuevas: fetch_california_housing). Compara LinearRegression con RandomForestRegressor en términos de MSE.


'''