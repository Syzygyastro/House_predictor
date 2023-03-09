from dash import html, dcc, Dash, dash_table, Input, Output
import dash_bootstrap_components as dbc
from iris_app.paralympic_dash_app import Line_graph
from iris_app.paralympic_dash_app import Scatter_plot
from iris_app.paralympic_dash_app import Violin_histogram
from iris_app.paralympic_dash_app import Bar_chart

def create_dash_app(flask_app):
    """Creates Dash as a route in Flask

    :param flask_app: A confired Flask app
    :return dash_app: A configured Dash app registered to the Flask app
    """
    # Register the Dash app to a route '/dashboard/' on a Flask app
    dash_app = Dash(
        __name__,
        server=flask_app,
        url_base_pathname="/dashboard/",
        meta_tags=[
            {
                "name": "viewport",
                "content": "width=device-width, initial-scale=1",
            }
        ],
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    dash_app.layout = html.Div([
        html.Div(Line_graph.line_layout()),
        html.Div(Scatter_plot.scatter_layout()),
        html.Div(Violin_histogram.violin_layout()),
        html.Div(Bar_chart.bar_layout())
    ])

    return dash_app
