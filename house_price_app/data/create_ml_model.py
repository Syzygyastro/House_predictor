from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle


def create_model(df, alg, pickle_file, house_type):
    """Creates a model using the linear regression algorithm provided. Output serialised using pickle.

    To make a prediction with the model:

    Args:
    df:DataFrame DataFrame containing the iris data
    alg:skickit-learn model object
    pickle_file:output file name and location
    house_type: string that will use data from the relevant coloumns in dataframe
    Returns:
    .pkl Pickled model

    """

    # Convert categorical data to numeric

    # X = feature value ("Date")
    X = df["Date"]
    # y = target values, last column of the data frame
    y = df[house_type]

    # Split the data into 80% training and 20% testing 
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    x_train = x_train.array.reshape(35, 1)
    x_test = x_test.array.reshape(9, 1)

    # Initialize the model
    model = alg
    # Train the model
    model.fit(x_train, y_train)

    print("Accuracy: ", model.score(x_test, y_test) * 100)

    # Test the model
    # print(x_test)
    # print(y_test)
    # print(predictions)
    # prediction = model.predict([[2020]])
    # print(prediction[0])
    # Pickle the model and save to the data folder
    pickle.dump(model, open(pickle_file, "wb"))


def main():
    """Create the models and serialise them."""
    iris_file = Path(__file__).parent.joinpath("house_prices_&_GDP_prepared.csv")
    iris_data = pd.read_csv(iris_file)
    iris_data = iris_data.drop(iris_data.index[0:20])

    model_lr = LinearRegression()

    pickle_file_all_lr = Path(__file__).parent.joinpath("model_all_lr.pkl")
    create_model(iris_data, model_lr, pickle_file_all_lr, "Price (All)")

    pickle_file_modern_lr = Path(__file__).parent.joinpath("model_modern_lr.pkl")
    create_model(iris_data, model_lr, pickle_file_modern_lr, "Price (Modern)")

    pickle_file_new_lr = Path(__file__).parent.joinpath("model_new_lr.pkl")
    create_model(iris_data, model_lr, pickle_file_new_lr, "Price (New)")

    pickle_file_older_lr = Path(__file__).parent.joinpath("model_old_lr.pkl")
    create_model(iris_data, model_lr, pickle_file_older_lr, "Price (Older)")


if __name__ == "__main__":
    main()
