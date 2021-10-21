from sklearn import preprocessing
import pandas as pd


df = pd.read_csv("data/dataset.csv")

df.head
df.dtypes
le = preprocessing.LabelEncoder()

label_encoded_df = df.copy()

label_encoded_df["brand"] = le.fit_transform(label_encoded_df["brand"])


label_encoded_df.head

le.inverse_transform([174])


for col in label_encoded_df.select_dtypes(include='O').columns:
    label_encoded_df[col] = le.fit_transform(label_encoded_df[col])

label_encoded_df.head

le.inverse_transform([25937])

label_encoded_df.dtypes
