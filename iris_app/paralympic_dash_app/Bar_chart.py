from dash import dcc, html  # pip install dash
import plotly.express as px
import pandas as pd                        # pip install pandas

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
df2 = pd.read_csv(r'iris_app/paralympic_dash_app/data/house_prices_quarterly_prepared.csv')
df2 = df2.drop(0)  # Following data has been removed as the particular year does not have all 4 seasons
df2 = df2.drop(249)
df2 = df2.drop(250)


def seasonal_house_price(price_type):
    '''
    Obtains a count of how much a certain type of house has its lowest price by each season

    Parameters
    ----------
    price_type: str
        Contains the name of the coloumn for the house price type from the prepared dataset
    Returns
    -------
    seasons: list
        list that contains an integer count of which season had the lowest price for that particular house type
    '''
    seasons = [0, 0, 0, 0]  # Initial count list
    for i in range(0, len(df2), 4):  # This for loop iterates every 4 rows of data (for the 4 seasons)
        # and then adds a count to whichever is highest
        prices = [df2.loc[i + 1][price_type], df2.loc[i + 2][price_type],
                  df2.loc[i + 3][price_type], df2.loc[i + 4][price_type]]
        min_price_index = prices.index(min(prices))
        seasons[min_price_index] += 1
    return seasons


prices = ["Average", "New", "Modern", "Old"]
seasons = ["Winter", "Spring", "Summer", "Autumn"]


# "data" Contains all the counts for the seasons for each house type
data = [seasonal_house_price("Price (All)"), seasonal_house_price("Price (New)"),
        seasonal_house_price("Price (Modern)"), seasonal_house_price("Price (Older)")]

seasonal_dic = {}

for i in range(len(prices)):  # Following creates a data frame for lowest house price with each type of house
    for j in range(len(seasons)):
        seasonal_dic[i*len(seasons) + j] = [prices[i], seasons[j], data[i][j]]
seasonal_df = pd.DataFrame.from_dict(seasonal_dic, orient='index')

fig = px.bar(seasonal_df, x=0, y=2, color=1, title="Comparing seasons for cheapest house prices", pattern_shape=1,
             pattern_shape_sequence=["/", "+", "x", "|"],
             labels={"0": "House Type",
                     "2": "No. times house prices were cheapest",
                     "1": "Season",
                     "Price (All)": "Average"})


def bar_layout():
    return html.Div([

        html.H4(children="Is there a certain season/month where house prices are the cheapest?", className="text-center"),

        dcc.Loading(dcc.Graph(figure=fig), type="cube"),

        html.Br(),
        ], className="centre")
