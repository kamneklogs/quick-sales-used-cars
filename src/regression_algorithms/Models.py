import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

ventas = pd.read_csv("ventas2.csv")
objetivo = "monto"
independientes = ventas.drop(columns=['monto']).columns

modelo = LinearRegression()
modelo.fit(X=ventas[independientes], y=ventas[objetivo])


ventas["ventas_prediccion"] = modelo.predict(ventas[independientes])
preds = ventas[["monto", "ventas_prediccion"]].head(50)


ventas.dtypes

ventas