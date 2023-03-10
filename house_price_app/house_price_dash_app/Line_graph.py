from dash import dcc, Output, Input, html
import plotly.express as px
import pandas as pd
import dash
df = pd.read_csv(r'house_price_app/house_price_dash_app/data/house_prices_&_GDP_prepared.csv')


dropdown = dcc.Dropdown(
                id="dropdown",
                options=[{"label": 'Average', "value": "Price (All)"},
                         {"label": "New", "value": "Price (New)"},
                         {"label": "Modern", "value": "Price (Modern)"},
                         {"label": "Old", "value": "Price (Older)"}],
                value='Price (All)',  # initial value displayed when page first loads
                clearable=False,
                className="centre3")
slider = dcc.RangeSlider(
            id="slider",
            marks={
                1952: "1952",     # key=position
                1960: "1960",
                1970: "1970",
                1980: "1980",
                1990: "1990",
                2000: "2000",
                2010: "2010",
                2015: {"label": "2015", "style": {"color": "#f50", "font-weight": "bold"}},

            },
            step=1,                # number of steps between values
            min=1952,
            max=2015,
            value=[1970, 2000],     # default value initially chosen
            dots=True,             # True, False - insert dots, only when step>1
            allowCross=False,      # True,False - Manage handle crossover
            disabled=False,        # True,False - disable handle
            pushable=2,            # any number, or True with multiple handles
            updatemode="mouseup",  # 'mouseup', 'drag' - update value method
            included=True,         # True, False - highlight handle
            vertical=False,        # True, False - vertical, horizontal slider
            verticalHeight=900,    # hight of slider (pixels) when vertical=True
            className="None",
            tooltip={"always_visible": False,  # show current slider values
                     "placement": "bottom"},
            )


# Callback allows components to interact
@dash.callback(
    Output("line_graph", "figure"),
    Input("dropdown", "value"),
    Input("slider", "value"))
def update_graph(column_name, range):
    '''
    Updates the plotly graph based on what dropdown is selected and what value the slider is on

    Parameters
    ----------
    coloumn_name : str
        Contains the name of the coloumn from the prepared dataset

    range: list
        Contains the two values for the slider range

    Returns
    -------
    fig: Plotly figure
        Graph of house prices against dates
    '''
    date_range_1 = df[df["Date"] == range[0]].index.values[0]
    date_range_2 = df[df["Date"] == range[1]].index.values[0]
    range_df = df[date_range_1:date_range_2]
    fig = px.line(data_frame=range_df, x="Date", y=column_name, title="House price fluctation from 1952 to 2015",
                  labels={"Price (All)": "House Price (£)",
                          "Price (New)": "New Type House Price (£)",
                          "Price (Modern)": "Modern Type House Price (£)",
                          "Price (Old)": "Old Type House Price (£)", })
    fig.update_traces(line_color='black', line_width=2)
    return fig


def line_layout():
    return html.Div([
        html.Br(),
        html.H4(children="Are house prices increasing with a steady progression?", className="text-center"),
        dcc.Loading(dcc.Graph(id="line_graph"), type="cube"),
        html.P("Filter by House type:", className="text-center"),
        dropdown,
        html.Br(),
        slider,
        html.Br(),
        html.Br(),])
