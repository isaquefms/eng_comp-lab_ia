import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('spambase.csv', sep=',', header=0)
# %matplotlib inline
sns.pairplot(data, hue='class')