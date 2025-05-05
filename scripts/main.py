from preprocessing import load_data
from plot_choropleth import make_choropleth
from plot_bubble import make_bubble
from plot_sunburst import make_sunburst
from plot_timeseries import make_timeseries
from plot_animated import make_animated
from plot_treemap import make_treemap
import plotly.io as pio
import os

# Optional: Set default renderer for interactive or static output
# pio.renderers.default = 'browser'  # Uncomment to open plots in browser

layout_style = dict(
    template='plotly_white',
    font=dict(family="Arial", size=14),
    title_font_size=20,
)

# Ensure output directory exists
os.makedirs("exports", exist_ok=True)

# Load data
df = load_data()

# Generate and show or export plots
plots = {
    "choropleth": make_choropleth(df, layout_style),
    "bubble": make_bubble(df, layout_style),
    "sunburst": make_sunburst(df, layout_style),
    "timeseries": make_timeseries(df, layout_style),
    "animated": make_animated(df, layout_style),
    "treemap": make_treemap(df, layout_style),
}

for name, fig in plots.items():
    fig.show()  # Display each plot interactively
    # Optional: Save as HTML
    fig.write_html(f"exports/{name}.html")
    print(f"Saved: exports/{name}.html")
