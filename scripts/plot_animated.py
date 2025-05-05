import plotly.express as px

def make_animated(df, layout_style):
    fig = px.scatter_geo(
        df,
        lat='plant_lat',
        lon='plant_lon',
        color='capacity_mw',
        size='capacity_mw',
        animation_frame='year',
        projection='natural earth',
        hover_name='name',
        title='Evolution of Hydropower Facilities Over Time',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(**layout_style)
    return fig
