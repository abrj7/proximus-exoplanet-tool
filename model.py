import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Constants
DATA_PATH = "exoplanets.csv"
MODEL_PATH = "habitability_model.pkl"

def load_and_preprocess_data():
    """
    Loads data and creates a target variable based on habitability criteria.
    """
    if not os.path.exists(DATA_PATH):
        print("Data file not found. Please run data_loader.py first.")
        return None

    df = pd.read_csv(DATA_PATH)
    
    # Drop rows with missing critical values
    df = df.dropna(subset=['pl_rade', 'pl_eqt', 'pl_insol', 'st_teff'])
    
    # Feature Engineering: Create a 'Habitability' label (Heuristic)
    # Criteria:
    # 1. Radius: 0.5 - 1.6 Earth Radii (Rocky)
    # 2. Equilibrium Temp: 200K - 320K (Liquid Water potential)
    # 3. Insolation Flux: 0.3 - 1.1 Earth Flux (Conservative HZ)
    
    def is_habitable(row):
        if (0.5 <= row['pl_rade'] <= 1.6) and \
           (200 <= row['pl_eqt'] <= 320) and \
           (0.3 <= row['pl_insol'] <= 1.1):
            return 1 # Potentially Habitable
        return 0 # Not Habitable

    df['habitable'] = df.apply(is_habitable, axis=1)
    
    print(f"Habitable planets in dataset: {df['habitable'].sum()} / {len(df)}")
    
    return df

def train_model(df):
    """
    Trains a Random Forest Classifier.
    """
    features = ['pl_rade', 'pl_eqt', 'pl_insol', 'st_teff']
    X = df[features]
    y = df['habitable']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate
    y_pred = clf.predict(X_test)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Save model
    joblib.dump(clf, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    df = load_and_preprocess_data()
    if df is not None:
        train_model(df)
