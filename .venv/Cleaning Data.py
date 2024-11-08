import pandas as pd

df = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python\pandasdata.csv")
''' dropna will return a new data frame by default and not change the original'''
'''remove rows'''
#new_df = df.dropna()
#print(new_df.to_string)
''' to change the original use inplace = True '''
#df.dropna(inplace = True)
#print(df.to_string)

'''replace empty values'''
#df.fillna(130, inplace=True)

'''replace in specified columns'''
#df["Calories"].fillna(130, inplace = True)
#print(df.to_string())
'''Calculate mean, median, mode'''
x = df["Calories"].mean()
y = df['Calories'].median()
z = df['Calories'].mode()
df['Calories'].fillna(x, inplace = True)



'''remove rows'''

#df.dropna(subset=['Date'], inplace = True)

'''replacing values, means replacing row 7 with value of 45'''
df.loc[7, 'Duration'] = 45

'''loop through values '''

for val in df.index:
    if df.loc[val, 'Duration'] > 120:
        df.loc[val, 'Duration'] = 120


'''Finding duplicates'''
#(df.duplicated())

'''Remove duplicates'''

df.drop_duplicates(inplace = True)


print(df.to_string())

