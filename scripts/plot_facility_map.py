# plot_facility_map.py
import plotly.express as px

def plot_facility_map(df):
    fig = px.scatter_mapbox(
        df, lat='lat', lon='lon',
        size='capacity_mw', color='capacity_mw',
        color_continuous_scale='Viridis',
        size_max=15, zoom=1,
        mapbox_style='carto-positron',
        title='Hydropower Facilities by Location and Capacity',
        labels={'capacity_mw': 'Capacity (MW)'}
    )
    fig.show()
