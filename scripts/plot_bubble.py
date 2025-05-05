import numpy as np
import plotly.express as px

def make_bubble(df, layout_style):
    df_bubble = df.dropna(subset=['res_vol_mcm'])
    fig = px.scatter_geo(
        df_bubble,
        lat='plant_lat',
        lon='plant_lon',
        size=np.sqrt(df_bubble['res_vol_mcm'] + 1),
        hover_name='name',
        hover_data={'capacity_mw': ':,.0f', 'res_vol_mcm': ':,.0f'},
        projection='natural earth',
        title='Hydropower Plants by Reservoir Volume'
    )
    fig.update_layout(**layout_style)
    return fig
