# plot_top_countries.py
import plotly.express as px

def plot_top_countries(df):
    country_cap = df.groupby('country', as_index=False)['capacity_mw'].sum().nlargest(10, 'capacity_mw')
    fig = px.bar(
        country_cap, x='country', y='capacity_mw',
        title='Top 10 Countries by Hydropower Capacity',
        color='capacity_mw', color_continuous_scale='Viridis',
        labels={'capacity_mw': 'Capacity (MW)', 'country': 'Country'}
    )
    fig.update_layout(xaxis_tickangle=-45)
    fig.show()
