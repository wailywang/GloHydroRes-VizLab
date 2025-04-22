# main.py
from load_data import load_and_clean_data
from plot_top_countries import plot_top_countries
from plot_year_distribution import plot_year_distribution
from plot_facility_map import plot_facility_map

if __name__ == '__main__':
    df = load_and_clean_data('GloHydroRes_vs1.csv')
    plot_top_countries(df)
    plot_year_distribution(df)
    plot_facility_map(df)
