from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine,types

# Define the database file name and location
db_file = Path(__file__).parent.joinpath("house_prices_&_GDP_prepared.db")

# Create a connection to file as a SQLite database (this automatically creates the file if it doesn't exist)
engine = create_engine("sqlite:///" + str(db_file), echo=False)
na_values = [
    "",
    "#N/A",
    "#N/A N/A",
    "#NA",
    "-1.#IND",
    "-1.#QNAN",
]
# Read the iris data to a pandas dataframe
house_price_file = Path(__file__).parent.joinpath("house_prices_&_GDP_prepared.csv")
house_price = pd.read_csv(house_price_file)
houses_prices = pd.read_csv(house_price_file,keep_default_na=False, na_values=na_values)
houses_prices = houses_prices.rename(columns={"Price (All)": "price_all", "Price (New)": "price_new",
                            "Price (Modern)": "price_modern", "Price (Older)": "price_old", "GDP": "gdp"})
# Write the data to tables in a sqlite database
dtype_noc = {
    "Date": types.INTEGER(),
    "price_all": types.FLOAT(),
    "price_new": types.FLOAT(),
    "price_modern": types.FLOAT(),
    "price_old": types.FLOAT(),
    "gdp": types.INTEGER(),
}
# Write the data to a table in the sqlite database (data/iris.db)
house_price.to_sql("house_prices_&_GDP_prepared", engine, if_exists="append", index=False)
houses_prices.to_sql("house_prices", engine, if_exists="append", index=False, dtype=dtype_noc)
