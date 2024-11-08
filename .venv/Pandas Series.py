import pandas as pd

''' a series is a column in a table'''
a = [1, 7, 2]

myvar = pd.Series(a)
#print(a)
#print(myvar)
#print(myvar[1])

'''with the index argument you can create your own labels'''
b = [1, 7, 2]
myvar_1 = pd.Series(b, index = ['x', 'y', 'z'])
#print(myvar_1)
#print(myvar_1['y'])

calories = {'Day 1' : 440, 'Day 2' : 560, 'Day 3' : 345}
'''Use the index argument to only select data you want to include'''
myvar_3 = pd.Series(calories, index = ['Day 1', 'Day 2'])

#print(myvar_3)


data = {
    'calories' : [560, 700, 345],
    'duration' : [50, 45, 40]
}

myvar_4 = pd.DataFrame(data)
print(myvar_4)
