from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

import pandas as pd


df = pd.read_csv("data/dataset_encoded.csv")

df
df.dtypes


objetivo = df['price']
independientes = df.drop(columns=['price']).columns


modelo = LinearRegression()
modelo.fit(X=df[independientes], y=df[objetivo])


talvez = modelo.predict([[41, 1, 1, 1]])
print("Tal vez compre: ")
print(talvez)
