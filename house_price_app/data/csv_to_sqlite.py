from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# Define the database file name and location
db_file = Path(__file__).parent.joinpath("house_prices_&_GDP_prepared.db")

# Create a connection to file as a SQLite database (this automatically creates the file if it doesn't exist)
engine = create_engine("sqlite:///" + str(db_file), echo=False)

# Read the iris data to a pandas dataframe
house_price_file = Path(__file__).parent.joinpath("house_prices_&_GDP_prepared.csv")
house_price = pd.read_csv(house_price_file)

# Write the data to a table in the sqlite database (data/iris.db)
house_price.to_sql("house_prices_&_GDP_prepared", engine, if_exists="append", index=False)

