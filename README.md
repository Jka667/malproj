# AI/ML Sentinel: PE Malware Watchdog / Sentinelle IA/ML : Gardien des Malwares PE


---

## English

### Overview
This project implements a simple AI/ML pipeline to classify Windows PE files (`.exe`, `.dll`) as **malware** or **benign** via static feature extraction and a RandomForest model. A Flask-based web interface provides an upload form and displays the result in a neon-green “hacker” theme.

**Author:** J0n4th4n.Kassegne  
**GitHub:** [Jka667](https://github.com/Jka667)

### Prerequisites
- **OS:** CentOS Stream 9 (VMware, Host-only or NAT)  
- **Python:** 3.10 or higher  
- **RAM:** ≥ 4 GB  
- **Disk:** ≥ 40 GB  

### Project Structure

malproj/
├── venv/                     # Python virtual environment
├── dataset/
│   ├── malware/              # Sample PE malware binaries
│   └── benign/               # Known-good .exe and .dll files
├── uploads/                  # Temporary upload folder (Flask)
├── extract_features.py       # Static feature extraction script
├── train_model.py            # Model training and saving script
├── predict.py                # CLI prediction script
├── malware_detector.pkl      # Serialized RandomForest model
├── app.py                    # Flask web application
├── templates/
│   └── index.html            # HTML template for upload form & result
└── static/
    └── style.css             # CSS 
Installation

# 1. Clone the repository
git clone https://github.com/Jka667/malproj.git
cd malproj

# 2. Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install required packages
pip install --upgrade pip
pip install pefile pandas scikit-learn joblib matplotlib jupyterlab flask
Command-line Usage
Extract features into CSV


python extract_features.py
# Output: malware_dataset.csv
Train the model and save it

bash
Copy
Edit
python train_model.py
# Prints classification report
# Saves model to malware_detector.pkl
Predict a single file


# Malware example
python predict.py dataset/malware/Win32.Wannacry.exe
# → Malware

# Benign example
python predict.py dataset/benign/calc.exe
# → Benign

# Non-PE / error case
python predict.py dataset/benign/test.txt
# → Unable to analyze the file
Web Interface
Run the Flask app


python app.py
Open your browser at http://127.0.0.1:5000/

Upload a .exe or .dll file and view the result on the page.

Security Notes
Do not execute any uploaded binary.

Always revert the VM to the CleanState snapshot after each analysis session.

Uploaded files are stored in uploads/ and removed immediately after analysis.

Français
Présentation
Ce projet propose un pipeline IA/ML simple qui classe des fichiers PE Windows (.exe, .dll) en malveillant ou bénin, via extraction statique de caractéristiques et un modèle RandomForest. Une interface web Flask, au style néon-vert “hacker”, permet d’uploader un fichier et d’afficher le résultat.

Auteur : J0n4th4n.K
GitHub : Jka667

Prérequis
OS : CentOS Stream 9 (VMware, Host-only ou NAT)

Python : 3.10 ou supérieur

RAM : ≥ 4 Go

Disque : ≥ 40 Go

Structure du projet

malproj/
├── venv/                     # Environnement virtuel Python
├── dataset/
│   ├── malware/              # Échantillons PE malveillants
│   └── benign/               # Fichiers .exe/.dll sains
├── uploads/                  # Dossier temporaire pour uploads (Flask)
├── extract_features.py       # Script d’extraction statique des caractéristiques
├── train_model.py            # Script d’entraînement et de sauvegarde du modèle
├── predict.py                # Script CLI de prédiction
├── malware_detector.pkl      # Modèle RandomForest sérialisé
├── app.py                    # Application web Flask
├── templates/
│   └── index.html            # Template HTML pour le formulaire et le résultat
└── static/
    └── style.css             # Feuille de style néon-vert “hacker”
Installation

# 1. Cloner le dépôt
git clone https://github.com/Jka667/malproj.git
cd malproj

# 2. Créer et activer l’environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 3. Installer les dépendances
pip install --upgrade pip
pip install pefile pandas scikit-learn joblib matplotlib jupyterlab flask
Utilisation en ligne de commande
Extraction vers CSV


python extract_features.py
# Génère : malware_dataset.csv
Entraînement et sauvegarde du modèle

bash
Copy
Edit
python train_model.py
# Affiche le rapport de classification
# Sauvegarde : malware_detector.pkl
Prédiction d’un fichier


# Exemple malware
python predict.py dataset/malware/Win32.Wannacry.exe
# → Malveillant

# Exemple bénin
python predict.py dataset/benign/calc.exe
# → Bénin

# Cas d’erreur (non-PE)
python predict.py dataset/benign/test.txt
# → Impossible d’analyser le fichier
Interface Web
Lancer l’application Flask


python app.py
Ouvrir votre navigateur à http://127.0.0.1:5000/

Téléverser un fichier .exe ou .dll et consulter le résultat.

Notes de sécurité
Ne jamais exécuter les binaires uploadés.

Revenir systématiquement au snapshot CleanState après chaque session.

Les fichiers téléversés sont supprimés immédiatement après analyse.
