import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python\pandasdata.csv")
'''Finds the correlation'''
df.corr()

df.plot(kind = 'scatter', x =  'Duration', y = 'Calories')
plt.show()

