import pandas as pd

'''Changes number of displayed rows'''
pd.options.display.max_rows = 9999

#df = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python\pandasdata.csv")

#print(df)

#df = pd.read_json(r"C:\Users\ellio\OneDrive\Desktop\Python\data.JSON")
#print(df)

df = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python\pandasdata.csv")
'''prints first 10 rows of the dataframe'''
#print(df.head(10))
'''prints last 10 rows of the dataframe'''
#print(df.tail(10))
'''information about the data'''
print(df.info())

