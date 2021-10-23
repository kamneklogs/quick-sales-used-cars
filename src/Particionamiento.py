import pandas as pd                #Importamos pandas para el manejo de los dataframes
import matplotlib.pyplot as plt    #Importamos pyplot de librería matplotlib. Lo vamos a utilizar para graficar.
import seaborn as sns              #Importamos la librería Seaborn. La vamos a utilizar para graficar.
import numpy as np                 #Importamos la librería numpy para manipular arreglos.
import random
from sklearn.model_selection import train_test_split

dfencoded = pd.read_csv("data/dataset_encoded.csv")


 y = df["price"] #Variable dependiente
 x = df.drop(columns="price") #Variables independiente

 x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.15, random_state= 42)

 x_train.head()

 y_train.head()
