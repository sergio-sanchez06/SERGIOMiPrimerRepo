'''
https://scikit-learn.org/stable/
https://www.datacamp.com/es/tutorial/machine-learning-python
https://www.digitalocean.com/community/tutorials/python-scikit-learn-tutorial
https://www.geeksforgeeks.org/machine-learning/scikit-learn-tutorial/
https://scikit-learn.org/1.4/tutorial/index.html
https://www.tutorialspoint.com/scikit_learn/index.htm

'''

from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

# 1. Clasificación básica en Iris
def ejercicio1():
    print("EJERCICIO 1: Regresión Logística en Iris")
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    print(f"Precisión en test: {model.score(X_test, y_test):.2f}\n")

# 2. Comparación de modelos en Digits
def ejercicio2():
    print("EJERCICIO 2: KNN vs SVM vs Random Forest (Digits)")
    digits = datasets.load_digits()
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)
    
    modelos = [KNeighborsClassifier(), SVC(), RandomForestClassifier()]
    for m in modelos:
        m.fit(X_train, y_train)
        score = accuracy_score(y_test, m.predict(X_test))
        print(f"{m.__class__.__name__} Accuracy: {score:.2f}")
    print("-" * 30)

# 3. Validación cruzada en Diabetes
def ejercicio3():
    print("EJERCICIO 3: Cross Validation (Diabetes)")
    diabetes = datasets.load_diabetes()
    model = LinearRegression()
    # cv=5 indica 5 grupos (folds)
    scores = cross_val_score(model, diabetes.data, diabetes.target, cv=5, scoring='neg_mean_squared_error')
    mse_medio = -scores.mean()
    print(f"MSE medio tras 5-fold CV: {mse_medio:.2f}\n")

# 4. Árbol de decisión en Iris
def ejercicio4():
    print("EJERCICIO 4: Árbol de Decisión y Visualización")
    iris = datasets.load_iris()
    clf = DecisionTreeClassifier(max_depth=3, random_state=42)
    clf.fit(iris.data, iris.target)
    plt.figure(figsize=(12,8))
    plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
    plt.title("Estructura del Árbol de Decisión (Iris)")
    plt.show()

# 5. Ajuste de hiperparámetros con GridSearchCV
def ejercicio5():
    print("EJERCICIO 5: GridSearchCV con SVC")
    iris = datasets.load_iris()
    parametros = {'C': [0.1, 1, 10, 100], 'kernel': ['linear', 'rbf']}
    grid = GridSearchCV(SVC(), parametros, cv=5)
    grid.fit(iris.data, iris.target)
    print(f"Mejores parámetros: {grid.best_params_}")
    print(f"Mejor precisión obtenida: {grid.best_score_:.2f}\n")

# 6. Clustering con KMeans
def ejercicio6():
    print("EJERCICIO 6: KMeans Clustering (Iris sin etiquetas)")
    iris = datasets.load_iris()
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(iris.data)
    # Comparación visual rápida
    print("Primeros 10 clusters predichos:", clusters[:10])
    print("Primeras 10 etiquetas reales:   ", iris.target[:10], "\n")

# 7. Reducción de dimensionalidad con PCA
def ejercicio7():
    print("EJERCICIO 7: PCA en Digits (de 64 a 2 dimensiones)")
    digits = datasets.load_digits()
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(digits.data)
    
    plt.figure(figsize=(8,6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=digits.target, cmap='tab10', alpha=0.6)
    plt.colorbar(label='Dígito')
    plt.title("Visualización de Digits con PCA")
    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.show()

# 8. Random Forest y importancia de características
def ejercicio8():
    print("EJERCICIO 8: Importancia de características (Breast Cancer)")
    cancer = datasets.load_breast_cancer()
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(cancer.data, cancer.target)
    
    importancias = pd.Series(rf.feature_importances_, index=cancer.feature_names).sort_values(ascending=False)
    print("Top 5 características que más influyen en el modelo:")
    print(importancias.head(5), "\n")

# 9. Pipeline completo
def ejercicio9():
    print("EJERCICIO 9: Pipeline (Escalado + Regresión)")
    wine = datasets.load_wine()
    mi_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression())
    ])
    res = cross_val_score(mi_pipeline, wine.data, wine.target, cv=5)
    print(f"Precisión media con Pipeline: {res.mean():.2f}\n")

# 10. Regresión con ensemble
def ejercicio10():
    print("EJERCICIO 10: Linear vs RandomForest (California Housing)")
    housing = datasets.fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target, test_size=0.2, random_state=42)
    
    # Modelos
    reg_lin = LinearRegression().fit(X_train, y_train)
    reg_rf = RandomForestRegressor(n_estimators=50, random_state=42).fit(X_train, y_train)
    
    # Evaluación
    mse_lin = mean_squared_error(y_test, reg_lin.predict(X_test))
    mse_rf = mean_squared_error(y_test, reg_rf.predict(X_test))
    
    print(f"MSE Regresión Lineal: {mse_lin:.2f}")
    print(f"MSE Random Forest:    {mse_rf:.2f}")

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