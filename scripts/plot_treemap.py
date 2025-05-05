import plotly.express as px

def make_treemap(df, layout_style):
    fig = px.treemap(
        df,
        path=['country', 'name'],
        values='capacity_mw',
        title='Treemap of Hydropower Capacity by Country and Facility'
    )
    fig.update_layout(**layout_style)
    return fig
