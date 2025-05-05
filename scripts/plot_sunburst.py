import plotly.express as px

def make_sunburst(df, layout_style):
    sun = df.groupby(['country', 'name'], as_index=False)['capacity_mw'].sum()
    fig = px.sunburst(
        sun,
        path=['country', 'name'],
        values='capacity_mw',
        title='Capacity Distribution by Country and Plant'
    )
    fig.update_layout(**layout_style)
    return fig
