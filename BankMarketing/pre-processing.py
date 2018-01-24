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


# Filling the unknown values of marital and job attributes with the mode
print("Mode of education = "+str(X['education'].mode()))
X['education'].fillna(X.education.mode()[0], inplace=True)
print("Mode of job = "+str(X['job'].mode()))
X['job'].fillna(X.job.mode()[0], inplace=True)


# Converting nominal data to numerical data
X['default'] = X['default'].map({'no':0, 'yes':1})
X['housing'] = X['housing'].map({'no':0, 'yes':1})
X['loan'] = X['loan'].map({'no':0, 'yes':1})
X['y'] = X['y'].map({'no':0, 'yes':1})
X['education'] = X['education'].map({'primary':1, 'secondary':2, 'tertiary':3})
X['marital'] = X['marital'].map({'single':1, 'married':2, 'divorced':3})
X['job'] = X['job'].map({'admin.':1, 'unemployed':2, 'management':3, 'housemaid':4, 'entrepreneur':5, 'student':6, 'blue-collar':7, 'self-employed':8, 'retired':9, 'technician':10, 'services':11})
X['month'] = X['month'].map({'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12})

print(X)
