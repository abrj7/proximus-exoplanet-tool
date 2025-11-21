from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os
import random

app = Flask(__name__)

# Load Data and Model
DATA_PATH = "exoplanets.csv"
MODEL_PATH = "habitability_model.pkl"

try:
    df = pd.read_csv(DATA_PATH)
    # Ensure we have a clean subset for display
    display_df = df.dropna(subset=['pl_name', 'pl_rade', 'pl_eqt', 'sy_dist']).head(20)
except Exception as e:
    print(f"Error loading data: {e}")
    display_df = pd.DataFrame()

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

import visualizer

@app.route('/')
def index():
    """Home page with planet carousel."""
    planets = display_df.to_dict(orient='records')
    return render_template('index.html', planets=planets)

@app.route('/planet/<planet_name>')
def planet_detail(planet_name):
    """Planet detail page."""
    planet = df[df['pl_name'] == planet_name].iloc[0].to_dict()
    
    # Generate visualization if needed
    try:
        visualizer.generate_planet_image(
            planet['pl_name'], 
            planet.get('pl_rade', 1.0), 
            planet.get('pl_eqt', 288)
        )
    except Exception as e:
        print(f"Error generating image for {planet_name}: {e}")

    return render_template('detail.html', planet=planet)

@app.route('/create')
def create_tool():
    """Exoplanet creation tool page."""
    return render_template('create.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint for the creation tool."""
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.json
        # Features: ['pl_rade', 'pl_eqt', 'pl_insol', 'st_teff']
        features = [
            float(data['radius']),
            float(data['temp']),
            float(data['flux']),
            float(data['star_temp'])
        ]
        
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0][1] # Prob of being habitable
        
        result = {
            'prediction': int(prediction),
            'probability': float(probability),
            'message': "Potentially Habitable" if prediction == 1 else "Likely Uninhabitable"
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
