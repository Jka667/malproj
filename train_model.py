import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("malware_dataset.csv")
X = df.drop(columns=['label'])
y = df['label']

# Séparation en jeu d'entraînement et jeu de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entraînement d'un modèle RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluation du modèle
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Sauvegarde du modèle entraîné
joblib.dump(model, 'malware_detector.pkl')
