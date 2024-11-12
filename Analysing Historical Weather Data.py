import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python\Cambridge NIAB.csv")

pd.set_option("display.max_rows", 5000)
pd.set_option('display.max_columns', 20)

#Removes certain rows from the data
df.drop(['status', 'Unnamed: 0', 'Tmin', 'Tmax', 'Date', 'AF'], axis = 1, inplace = True)

for val in df.index:
    if df.loc[val, 'Month'] > 1:
        df.loc[val, 'Month'] = 0

# Removes values based on a list
list = [0]
df = df[df.Month.isin(list) == False]

#plotting the mean temp
df.plot(x = 'Year', y = 'Tmean')
plt.ylabel('Temp')
df.plot(x = 'Year')
plt.grid()
plt.show()









