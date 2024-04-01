# -*- coding: utf-8 -*-


from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

data_test = pd.read_csv("play_tennis_test.csv")
data_train = pd.read_csv("play_tennis_train.csv")

data_train

data_test

le = preprocessing.LabelEncoder()
data_train_df = pd.DataFrame(data_train)
data_train_df_encoded = data_train_df.apply(le.fit_transform)

data_test_df = pd.DataFrame(data_test)
data_test_df_encoded = data_test_df.apply(le.fit_transform)

X_train = data_train_df_encoded.drop(['play'],axis=1)
y_train = data_train_df_encoded['play']

X_test = data_test_df_encoded.drop(['play'],axis=1)
y_test = data_test_df_encoded['play']

X_train

y_train

classifier = GaussianNB()
model = classifier.fit(X_train, y_train)

y_pred = model.predict(X_test)

model.predict(X_test)

y_test

X_test = np.array([[2, 1, 0, 0],  #Outlook: Rainy, Temp: Mild, Humidity: High, Wind: Weak
                   [1, 1, 1, 0]]) #Outlook: Sunny, Temp: Mild, Humidity: High, Wind: Weak

X_test = np.array([[2, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 1, 0, 1, 0]])
predictions = classifier.predict(X_test)
print(predictions)

