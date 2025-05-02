from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
import pandas as pd
from math import pi


def generate_plot(data: dict) -> figure:
    """
    Generate a pie chart using Bokeh.

    Args:
        data (dict): A dictionary containing the data to plot.

    Returns:
        figure: A Bokeh figure object.
    """
    # Prepare data for pie chart
    data = pd.Series(data).reset_index(name='value').rename(
        columns={'index': 'category'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(data)]

    # Create a Bokeh figure
    p = figure(height=350, title="Distribution expenses", toolbar_location=None,
               tools="hover", tooltips="@category: @value{0.00}", x_range=(-0.5, 1.0))

    # Add wedges to the figure
    p.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'), line_color="white", fill_color='color', legend_field='category', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    return p
