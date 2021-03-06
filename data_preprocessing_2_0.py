# -*- coding: utf-8 -*-
"""data_preprocessing_2.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HJPC5rfCCfVWtNI7SNYwvoFFmIRIJzSy
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

print(x)

print(y)

#missing data  processing

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

x

#categorical data
#oneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
#By specifying remainder='passthrough' , all remaining columns that were not specified in transformers will be automatically passed through
x=np.array(ct.fit_transform(x))

# ColumnTransformer returns numpy.array

print(x)

#encoding dependent variable

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
y=l.fit_transform(y)

print(y)

#splitting dataset into training set and testing sets

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Hi, The number "42" was apparently chosen as a tribute to the "Hitch-hiker's Guide" books by Douglas Adams, as it was supposedly the answer to the great question of "Life, the universe, and everything" as calculated by a computer (named "Deep Thought") created specifically to solve it.
# the random_state parameter is used for initializing the internal random number generator, which will decide the splitting of data into train and test indices in your case. ... Setting random_state a fixed value will guarantee that the same sequence of random numbers is generated each time you run the code.

print(x_train)

print(x_test)

print(y_train)

print(y_test)

#feature scaling

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train[:,3:]=sc.fit_transform(x_train[:,3:])
x_test[:,3:]=sc.transform(x_test[:,3:])

print(x_train)

print(x_test)

print(y_train)

print(y_test)

