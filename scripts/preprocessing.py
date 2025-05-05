import pandas as pd
import pycountry

def iso3(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except LookupError:
        return None

def load_data(filepath="GloHydroRes_vs1.csv"):
    df = pd.read_csv(filepath)
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['capacity_mw'] = pd.to_numeric(df['capacity_mw'], errors='coerce')
    df['res_vol_mcm'] = df['res_vol_km3'] * 1000 if 'res_vol_km3' in df.columns else pd.NA
    df['Country_Iso3'] = df['country'].map(iso3)
    df = df.dropna(subset=['plant_lat', 'plant_lon'])
    return df
