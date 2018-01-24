import numpy as np
import pandas as pd

X = pd.read_csv("bank/bank-full.csv", delimiter=';')

# Replace all unknown values with nan
X = X.replace("unknown",np.nan)


# Delete some values of age attribute
cnt=0
for i in range(len(X)):
    if i%1000 == 0:
        X = X.replace(X['age'][i], np.nan)
        cnt = cnt+1
print("Total number of Missing Values in Age attribute = "+str(cnt))


# Filling the missing values with Mean of the age
print("Median Age = "+str(X["age"].median()))
X['age'].fillna(X.age.median(), inplace=True)


# Filling the unknown values of marital attribute with the mode
print("Mode of education = "+str(X['education'].mode()))
X['education'].fillna(X.education.mode()[0], inplace=True)


# Replacing yes and no with 1 and 0
X['default'] = X['default'].map({'no':0, 'yes':1})
X['housing'] = X['housing'].map({'no':0, 'yes':1})
X['loan'] = X['loan'].map({'no':0, 'yes':1})
X['y'] = X['y'].map({'no':0, 'yes':1})

X['education'] = X['education'].map({'primary':1, 'secondary':2, 'tertiary':3})
print(X)
