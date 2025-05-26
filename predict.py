import joblib
from extract_features import extract_features
import pandas as pd
import sys

model = joblib.load('malware_detector.pkl')

def predict_file(path):
    feats = extract_features(path)
    if feats:
        df = pd.DataFrame([feats])
        prediction = model.predict(df)[0]
        return "Malware ⚠️" if prediction == 1 else "Benign ✅"
    else:
        return "Impossible d'analyser le fichier 🚫"

if __name__ == "__main__":
    file_path = sys.argv[1]  # Fichier à analyser donné en argument
    result = predict_file(file_path)
    print(f"Résultat pour {file_path}: {result}")
