# plot_year_distribution.py
import plotly.express as px

def plot_year_distribution(df):
    fig = px.histogram(
        df, x='year', nbins=30,
        title='Distribution of Commissioning Years',
        labels={'year': 'Commissioning Year', 'count': 'Number of Facilities'},
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig.show()
