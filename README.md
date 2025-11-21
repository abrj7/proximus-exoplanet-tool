# Proximus Exoplanet Application

Proximus is a web application designed to visualize exoplanets and predict their habitability using Machine Learning. Leveraging data from the NASA Exoplanet Archive, it provides an interactive interface for exploring the cosmos and analyzing the potential for life on distant worlds.

> **Note:** This project was originally conceived as an offline application. However, during development, the decision was made to evolve it into a full-featured web application. This shift allowed us to leverage the dynamic capabilities of modern web frameworks and real-time data integration, which proved difficult to achieve within the constraints of a strictly offline environment.

## Features

*   **Real-Time Data Integration**: Fetches the latest confirmed exoplanet data directly from the NASA Exoplanet Archive.
*   **Habitability Prediction Engine**: Utilizes a Random Forest Classifier (Scikit-learn) to analyze planet parameters (Radius, Temperature, Insolation Flux) and predict the likelihood of habitability.
*   **3D Visualization**: Generates unique, scientifically-inspired 3D textured spheres for each planet using Matplotlib.
*   **Exoplanet Creation Tool**: An interactive module where users can design their own planets and test them against the ML model.
*   **Premium UI/UX**: Features a modern, dark-themed aesthetic with glassmorphism effects and smooth animations to provide an immersive experience.

## Tech Stack

*   **Backend**: Python, Flask
*   **Machine Learning**: Scikit-learn, Pandas, NumPy
*   **Visualization**: Matplotlib
*   **Frontend**: HTML5, CSS3 (Custom Design System), JavaScript

## Installation & Setup

1.  **Clone the repository**:
    ```bash

    git clone https://github.com/yourusername/proximus-exoplanet.git
    cd proximus-exoplanet
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Initialize Data**:
    Fetch the latest data from NASA or generate the fallback dataset.
    ```bash
    python data_loader.py
    ```

4.  **Train the Model**:
    Train the Random Forest model on the fetched data.
    ```bash
    python model.py
    ```

5.  **Run the Application**:
    Start the Flask development server.
    ```bash
    python app.py

    ```
    The application will be accessible at `http://localhost:5001`.

## Project Statistics

*   **Data Source**: NASA Exoplanet Archive
*   **Planets Analyzed**: 5,500+
*   **Model Accuracy**: ~75% (on test set)

## App Demo
<img width="223" height="454" alt="Screenshot 2025-11-21 at 2 00 28 AM" src="https://github.com/user-attachments/assets/f104deb7-fbbb-4854-9fc3-0d317f06c1f2" />
<img width="203" height="414" alt="Screenshot 2025-11-21 at 2 00 58 AM" src="https://github.com/user-attachments/assets/9523e6d1-0882-4049-a5f9-23c2af8ba636" />
<img width="203" height="414" alt="Screenshot 2025-11-21 at 2 01 44 AM" src="https://github.com/user-attachments/assets/cbc5a40d-8cd4-4023-aa8f-92d88f1be0dc" />
<img width="203" height="414" alt="Screenshot 2025-11-21 at 2 02 57 AM" src="https://github.com/user-attachments/assets/c86385a8-1e12-4d57-a8f9-0383554133c7" />


