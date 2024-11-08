import pandas as pd


data = {
    'calories' : [560, 700, 345],
    'duration' : [50, 45, 40]
}
'''index gives names to rows'''
df = pd.DataFrame(data, index = ['Day 1', 'Day 2', 'Day 3'])
#print(df)
'''to locate row '''
#print(df.loc[0])
print(df.loc['Day 2'])

