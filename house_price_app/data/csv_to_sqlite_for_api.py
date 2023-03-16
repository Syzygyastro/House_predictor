from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, types


# Define the database file name and location
db_file = Path(__file__).parent.joinpath("House_price.db")
# Create a connection to file as a SQLite database (this automatically creates the file if it doesn't exist)
engine = create_engine("sqlite:///" + str(db_file), echo=False)

# Read the noc_regions data to a pandas dataframe
# The following avoids an issue whereby entries with "NA" in the csv file are treated as null values rather than valid text 'NA' which is what we want
na_values = [
    "",
    "#N/A",
    "#N/A N/A",
    "#NA",
    "-1.#IND",
    "-1.#QNAN",
]

noc_file = Path(__file__).parent.joinpath("house_prices_&_GDP_prepared.csv")
# Read the data and handles the NA issue
noc_regions = pd.read_csv(noc_file, keep_default_na=False, na_values=na_values)
noc_regions = noc_regions.rename(columns={"Price (All)": "price_all", "Price (New)": "price_new",
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

noc_regions.to_sql(
    "house_prices", engine, if_exists="replace", index=False, dtype=dtype_noc
)