from dash import dcc, Output, Input, html  # pip install dash
import plotly.express as px
import pandas as pd
import dash

initial_df = pd.read_csv(r'iris_app/paralympic_dash_app/data/house_prices_&_GDP_prepared.csv')


def manipulate_df(dataframe):

    '''
    Manipulates the original dataframe to create a suitable format for the scatter plot

    Parameters
    ----------
    dataframe: Pandas DataFrame
        Contains pandas dataframe which is required to be manipulated.

    Returns
    ----------
    final_df: Pandas DataFrame
        Final dataframe suitable for the scatter plot
    '''

    dataframe = dataframe.set_index('Date')
    df_1 = dataframe.loc[1952:1967]
    df_2 = dataframe.loc[1968:1984]
    df_3 = dataframe.loc[1985:2001]
    df_4 = dataframe.loc[2002:2015]
    df_list = [df_1, df_2, df_3, df_4]
    year_range = ['1952-1967', '1968-1984', '1985-2001', '2002-2015']
    for i in range(0, len(df_list)):
        df_list[i].insert(loc=1,
                          column='Year range',
                          value=year_range[i])
    final_df = pd.concat(df_list)
    return final_df


df = manipulate_df(initial_df)


def scatter_layout():

    return html.Div([
                html.H4('How much are house prices affected by the economic state of the country', className="text-center"),
                dcc.Loading(dcc.Graph(id="scatter_graph"), type="cube"),
                html.P("Filter by House type:", className="text-center"),
                dcc.Dropdown(
                    id="scatter_dropdown",
                    options=[{"label": 'Average', "value": "Price (All)"},
                             {"label": "New", "value": "Price (New)"},
                             {"label": "Modern", "value": "Price (Modern)"},
                             {"label": "Old", "value": "Price (Older)"}],
                    value=["Price (All)"],
                    multi=True,
                    clearable=False,
                    style={'width': "60%", "margin-left": "auto", "margin-right": "auto"},
                    placeholder="Select a house type",
                ),
                html.Br(),
                html.Br(),])


@dash.callback(
    Output("scatter_graph", "figure"),
    Input("scatter_dropdown", "value"))
def update_scatter_plot(x):
    '''
    Plots the scatter plot graphs to anlayse correlations between differnt house types with GDP

    Parameters
    ----------
    x: str
        Gives column names to extract from dataframe, which is used as the x axis in the scatter plot

    Returns
    ----------
    fig: Plotly figure
        Scatter plot of house prices against GDP
    '''

    fig = px.scatter(
        df, x=x, y='GDP', title="Comaparing correlations of house prices and GDP", trendline='ols', labels={
                     "value": 'House Price (£)',
                     "variable": 'House type',
                     'GDP': 'GDP (£)'
                     })
    fig.update_traces(
                    marker=dict(symbol="diamond", size=9, line=dict(width=2.4, color="Black")),
                    selector=dict(mode="markers"))

    return fig
