from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


import numpy as np  # linear algebra

import pandas as pd


df = pd.read_csv("data/dataset_encoded.csv")
df.dtypes

df = df.astype({"doors": int, "kilometers": int, "year": int, "price": int})
objetivo = "price"
independientes = df.drop(columns=['price']).columns


modelo = LinearRegression()
modelo.fit(X=df[independientes], y=df[objetivo])


df["ventas_prediccion"] = modelo.predict(df[independientes])
preds = df[["price", "ventas_prediccion"]].head(50)


preds

df


talvez = modelo.predict(
    [[9, 79, 41, 31, 5, 1, 10000, 739, 227, 5, 0, 2020]])


print("Precio recomendado: ")
print(talvez)


print("Coeficiente de determinación R^2:",
      modelo.score(df[independientes], df[objetivo]))
