import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('house_prices_&_GDP_prepared.csv')
dataset = dataset.drop(dataset.index[0:20])


def predicting_houseprice(year, house_type):
    X = dataset[["Date"]]
    y = dataset[[house_type]]

    regressor = LinearRegression()
    regressor.fit(X, y)

    predicted_houseprice = year*(regressor.coef_[0]) + regressor.intercept_[0]
    predicted_houseprice = int(round(predicted_houseprice[0],0))
    return predicted_houseprice

print(predicting_houseprice(2024, "Price (All)"))
#print(int(round(predicted_houseprice[0],0)))
# print(regressor.intercept_)
# print(regressor.coef_)
# plt.scatter(X, y, color = 'red')
# plt.plot(X, regressor.predict(X), color = 'blue')
# plt.title('mark1 vs mark2')
# plt.xlabel('mark1')
# plt.ylabel('mark2')
# plt.show()