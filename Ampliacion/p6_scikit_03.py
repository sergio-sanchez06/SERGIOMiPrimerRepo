import arff  # Instala con: pip install liac-arff
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Cargar el archivo ARFF
with open('iris.arff', 'r') as f:
    dataset = arff.load(f)

# Extraer los datos y los nombres de atributos
data = np.array(dataset['data'])
attributes = [attr[0] for attr in dataset['attributes']]

# Separar características (X) y etiquetas (y)
X = data[:, :-1].astype(float)
y = data[:, -1]

# Convertir etiquetas de texto a números
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.5, random_state=42)

# Entrenar RandomForest
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Calcular métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')

