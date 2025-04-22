# load_data.py
import pandas as pd

def load_and_clean_data(path='GloHydroRes_vs1.csv'):
    df = pd.read_csv(path)
    df = df.assign(
        year=lambda d: pd.to_numeric(d['year'], errors='coerce'),
        capacity_mw=lambda d: pd.to_numeric(d['capacity_mw'], errors='coerce'),
        lat=lambda d: pd.to_numeric(d['plant_lat'], errors='coerce'),
        lon=lambda d: pd.to_numeric(d['plant_lon'], errors='coerce')
    ).dropna(subset=['country', 'year', 'capacity_mw', 'lat', 'lon'])
    return df
