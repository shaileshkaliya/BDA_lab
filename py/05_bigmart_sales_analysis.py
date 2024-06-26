# -*- coding: utf-8 -*-
"""5_BigMart_Sales_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bUsVKwzxqK6_uWii1whblDpRZm0KCEvq
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt     # is a collection of command style functions that make matplotlib work like MATLAB
import seaborn as sns

df_train= pd.read_csv('train_bigmart.csv')
df_test= pd.read_csv('test_bigmart.csv')

df_train.head()  # displays the first five rows of the dataframe by default

df_test.head()

df_train.shape  # a tuple of array dimensions that tells the number of rows and columns of a given DataFrame

df_train.isnull().sum()  #seeing the number of null values in the dataset

df_test.isnull().sum()

df_train.info()   #seeing the detailed info of the dataset and its types of target variables

df_train.describe()  # to generate descriptive statistics that summarize the central tendency, dispersion and
                     # shape of a dataset's distribution, excluding NaN values.

"""## Item_Weight is numerical column so we fill it with Mean Imputation"""

df_train['Item_Weight'].describe()  #seeing all the central tendenies of the dataset

df_train['Item_Weight'].fillna(df_train['Item_Weight'].mean(),inplace=True)  #replacing null values with mean values
df_test['Item_Weight'].fillna(df_train['Item_Weight'].mean(),inplace=True)

df_train.isnull().sum()  #no null values in item weight

df_train['Item_Weight'].describe()

"""## Outlet_Size is catagorical column so we fill it with Mode Imputation"""

df_train['Outlet_Size']  #it is a categorical value

df_train['Outlet_Size'].value_counts()

df_train['Outlet_Size'].mode()

df_train['Outlet_Size'].fillna(df_train['Outlet_Size'].mode()[0],inplace=True)
df_test['Outlet_Size'].fillna(df_test['Outlet_Size'].mode()[0],inplace=True)

df_train.isnull().sum()  #no null value :)

df_test.isnull().sum()

"""# Dimesnsionality reduction of item identifier and outlet identifier"""

df_train.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)
df_test.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)

df_test

"""## Preprocessing Task before Model Building

## 1) Label encoding
"""

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df_train['Item_Fat_Content']= le.fit_transform(df_train['Item_Fat_Content'])
df_train['Item_Type']= le.fit_transform(df_train['Item_Type'])
df_train['Outlet_Size']= le.fit_transform(df_train['Outlet_Size'])
df_train['Outlet_Location_Type']= le.fit_transform(df_train['Outlet_Location_Type'])
df_train['Outlet_Type']= le.fit_transform(df_train['Outlet_Type'])

df_train.head(5)

"""## 2) Splitting our data into train and test files"""

X=df_train.drop('Item_Outlet_Sales',axis=1)

Y=df_train['Item_Outlet_Sales']

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=101, test_size=0.2)

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

"""## Linear Regression"""

from sklearn.linear_model import LinearRegression
lr= LinearRegression()

lr.fit(X_train,Y_train)

Y_pred_lr=lr.predict(X_test)

print(r2_score(Y_test,Y_pred_lr))
print(mean_absolute_error(Y_test,Y_pred_lr))
print(np.sqrt(mean_squared_error(Y_test,Y_pred_lr)))