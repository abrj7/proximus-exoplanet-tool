import pandas as pd
import requests
import io
import os

# NASA Exoplanet Archive TAP URL
# We will use a public query to fetch confirmed planets with specific columns
DATA_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_rade,pl_eqt,pl_insol,st_teff,st_rad,sy_dist+from+ps+where+default_flag=1+and+pl_rade+is+not+null+and+pl_eqt+is+not+null&format=csv"

LOCAL_DATA_PATH = "exoplanets.csv"

def fetch_data():
    """
    Fetches data from the NASA Exoplanet Archive or loads from a local file.
    Returns a pandas DataFrame.
    """
    if os.path.exists(LOCAL_DATA_PATH):
        print(f"Loading data from local file: {LOCAL_DATA_PATH}")
        return pd.read_csv(LOCAL_DATA_PATH)

    print("Fetching data from NASA Exoplanet Archive...")
    try:
        response = requests.get(DATA_URL, timeout=30)
        response.raise_for_status()
        content = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(content))
        
        # Save to local for caching
        df.to_csv(LOCAL_DATA_PATH, index=False)
        print(f"Data fetched and saved to {LOCAL_DATA_PATH}")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        print("Falling back to mock data...")
        return create_mock_data()

def create_mock_data():
    """
    Creates a mock dataset for demonstration if the API fails.
    """
    data = {
        'pl_name': ['Kepler-452 b', 'Proxima Centauri b', 'TRAPPIST-1 e', 'Earth', 'Mars (Mock)', 'Jupiter (Mock)'],
        'pl_rade': [1.63, 1.07, 0.92, 1.00, 0.53, 11.2],  # Radius (Earth radii)
        'pl_eqt': [265, 234, 251, 255, 210, 110],         # Equilibrium Temp (K)
        'pl_insol': [1.1, 0.65, 0.66, 1.00, 0.43, 0.04],  # Insolation Flux (Earth flux)
        'st_teff': [5757, 3042, 2566, 5780, 5780, 5780],  # Star Temp (K)
        'st_rad': [1.11, 0.14, 0.12, 1.00, 1.00, 1.00],   # Star Radius (Solar radii)
        'sy_dist': [561, 1.3, 12.1, 0, 0, 0]              # Distance (pc)
    }
    df = pd.DataFrame(data)
    df.to_csv(LOCAL_DATA_PATH, index=False)
    return df

if __name__ == "__main__":
    df = fetch_data()
    print(df.head())
    print(f"Total planets: {len(df)}")
