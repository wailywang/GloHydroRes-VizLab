import plotly.express as px

def make_choropleth(df, layout_style):
    country_cap = df.groupby('Country_Iso3', as_index=False)['capacity_mw'].sum()
    fig = px.choropleth(
        country_cap,
        locations='Country_Iso3',
        color='capacity_mw',
        title='Total Hydropower Capacity by Country (MW)',
        color_continuous_scale='Cividis'
    )
    fig.update_layout(**layout_style)
    return fig
