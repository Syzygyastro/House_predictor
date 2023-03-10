from dash import dcc, Output, Input, html
import plotly.express as px
import pandas as pd
import dash

df = pd.read_csv(r'house_price_app/house_price_dash_app/data/house_prices_quarterly_prepared.csv')
temp_df = pd.read_csv(r'house_price_app/house_price_dash_app/data/house_prices_initial.csv')
temp_df = temp_df[['Date', 'Change (All)', 'Change (New)', 'Change (Modern)', 'Change (Older)']]
df = df[['Date', 'Price (All)', 'Price (New)', 'Price (Modern)', 'Price (Older)']]


def prepare_df(dataframe, temp_df):
    '''
    Creates a dictionary which is in a suitable format for a violin plot

    Parameters
    ----------
    dataframe: Pandas DataFrame
        First dataframe required for the final dictionary
    temp_df: Pandas DataFrame
        Second dataframe required for the final dictionary

    Returns
    ----------
    price_dic: Dictionary
        Final dictionary which is in the correct format for violin plot
    '''

    dataframe = dataframe.merge(temp_df, on='Date', how='left')
    dataframe = dataframe.drop(range(0, 4))
    change_new = list(dataframe["Change (New)"])
    change_modern = list(dataframe["Change (Modern)"])
    change_older = list(dataframe["Change (Older)"])
    date = list(dataframe["Date"])
    house_type_str = ['New', 'Modern', 'Older']
    house_type_values = [change_new, change_modern, change_older]
    price_dic = {}
    for x in range(0, len(house_type_str)):
        for i in range(0, len(change_new)):
            if x == 0:
                price_dic[i] = [house_type_str[x], house_type_values[x][i], date[i], 'New']
            elif x == 1:
                price_dic["2."+str(i)] = [house_type_str[x], house_type_values[x][i], date[i], 'Modern']
            else:
                price_dic["3."+str(i)] = [house_type_str[x], house_type_values[x][i], date[i], 'Old']
    return price_dic


price_dic = prepare_df(df, temp_df)

# Converting dictionary to pandas dataframe
price_change_df = pd.DataFrame.from_dict(price_dic, orient='index',
                                         columns=['House type', 'Percentage change', 'Date', 'Type'])


def violin_layout():
    return html.Div([
            html.H4('How do house prices vary per year?', className="text-center"),
            html.Br(),
            dcc.RadioItems(
                id='selection',
                options=["Histogram", "Violin"],
                value='Histogram',
                labelStyle={'display': 'block'},
                style={"textAlign": "centre"},
            ),
            dcc.Loading(dcc.Graph(id="histogram_graph"), type="cube"),],
            className="centre2")


@dash.callback(
    Output("histogram_graph", "figure"),
    Input("selection", "value"))
def display_graph(chosen_plot):
    '''
    Plots the scatter plot graphs to anlayse correlations between differnt house types with GDP

    Parameters
    ----------
    chosen_plot: str
        Either "Histogram" or "Violin". Determines which plot will be returned based on user input

    Returns
    ----------
    plots: Plotly figure
        Returns either histogram or violin plot on analysis of price variations per year
    '''
    plots = {
        'Histogram': px.histogram(price_change_df, x="Percentage change", color='House type', labels={
                    "Percentage change": 'Percentage change (%)'}).update_layout(yaxis_title="Frequency"),
        'Violin': px.violin(price_change_df, y='Percentage change', x='House type', box=True, points="all", labels={
                    "Percentage change": 'Percentage change (%)'}
                    ),

    }
    return plots[chosen_plot]
