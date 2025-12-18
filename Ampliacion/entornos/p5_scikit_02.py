import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Cargar el dataset
df = pd.read_csv('titanic.csv')

# Preprocesamiento básico
# Seleccionamos columnas relevantes y manejamos valores nulos
features = ['Passengerid', 'Age','Fare','Sex','sibsp', 'Parch', 'Embarked']
df = df[features + ['Survived']]

# Rellenar valores nulos en 'Age' y 'Fare' con la mediana
#df['Age'].fillna(df['Age'].median(), inplace=True)
#df['Fare'].fillna(df['Fare'].median(), inplace=True)

# Rellenar valores nulos en 'Embarked' con la moda
#df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Convertir variables categóricas a numéricas
#df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'])

# Separar variables independientes y dependiente
X = df.drop('Survived', axis=1).values
y = df['Survived'].values

# Inicializar el clasificador y la validación cruzada
clf = DecisionTreeClassifier(random_state=42)
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

accuracies = []
precisions = []
recalls = []

for train_idx, test_idx in skf.split(X, y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))
    precisions.append(precision_score(y_test, y_pred))
    recalls.append(recall_score(y_test, y_pred))

print(f'Accuracy promedio: {np.mean(accuracies):.2f}')
print(f'Precision promedio: {np.mean(precisions):.2f}')
print(f'Recall promedio: {np.mean(recalls):.2f}')

