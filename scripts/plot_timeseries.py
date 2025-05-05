import plotly.graph_objects as go

def make_timeseries(df, layout_style, selected=None):
    df_ts = df.dropna(subset=['year', 'country', 'capacity_mw'])
    yearly_country = df_ts.groupby(['country', 'year'], as_index=False)['capacity_mw'].sum()
    countries = sorted(yearly_country['country'].dropna().unique())
    if selected is None:
        selected = [c for c in ['China', 'United States'] if c in countries]
    fig = go.Figure()
    for country in selected:
        data = yearly_country[yearly_country['country'] == country]
        fig.add_trace(go.Scatter(
            x=data['year'],
            y=data['capacity_mw'],
            mode='lines',
            name=country,
            hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Capacity: %{y:.2f} MW',
            text=[country]*len(data),
        ))
    fig.update_layout(
        title='Installed Capacity by Country Over Time',
        xaxis_title='Year',
        yaxis_title='Installed Capacity (MW)',
        hovermode='x unified',
        **layout_style
    )
    return fig
