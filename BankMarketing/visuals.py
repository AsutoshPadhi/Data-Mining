import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from preProcessing import preProcessor

X = preProcessor()
# age = []
# y = []
# age = np.array(X['age'])
# y = np.array(X['y'])
# print(age)
X['age'].hist(bins=10)
print(X.dtypes)
plt.show()