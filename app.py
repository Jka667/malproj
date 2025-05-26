from flask import Flask, request, render_template
import pandas as pd
import joblib
import os
from extract_features import extract_features

app = Flask(__name__, static_folder="static")
model = joblib.load("malware_detector.pkl")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            feats = extract_features(path)
            if feats:
                df = pd.DataFrame([feats])
                pred = model.predict(df)[0]
                prediction = "M4lw4r3 ⚠️" if pred == 1 else "B3n1gn ✅"
            else:
                prediction = "3rr3ur d’4n4lys3 🚫"
            os.remove(path)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
