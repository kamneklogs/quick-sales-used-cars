import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/dataset.csv")


print(df)

df1 = df.pop('price')

df['price'] = df1

print(df)


class MultiColumnLabelEncoder:

    def __init__(self, columns=None):
        self.columns = columns  # array of column names to encode
        self.le = LabelEncoder()

    def fit(self, X, y=None):
        return self  # not relevant here

    def transform(self, X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = self.le.fit_transform(output[col])
        else:
            for colname, col in output.iteritems():
                output[colname] = self.le.fit_transform(col)
        return output

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)

    def inverse_transform(self, X):
        return self.le.inverse_transform(X)


mcle = MultiColumnLabelEncoder(columns=['bodywork_type', 'brand', 'city',
                                        'color', 'fuel_type', 'model', 'motor', 'state', 'transmission'])

print(mcle)
df = mcle.fit_transform(df)

print(df)

inverse = mcle.inverse_transform(df['transmission'])
print(df['transmission'])

type(df['transmission'].values)
type(inverse)

print(inverse)

transmissionDict = {}
for A, B in zip(df['transmission'].values, inverse):
    transmissionDict[A] = B

print(transmissionDict)


df.to_csv('data/dataset_encoded.csv')
