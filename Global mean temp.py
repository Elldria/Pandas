import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python_CSV\gmt_NOAAGlobalTemp.csv")
df_2 = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python_CSV\gmt_HadCRUT5.csv")
df_3 = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python_CSV\gmt_GISTEMP.csv")
df_4 = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python_CSV\gmt_Berkeley Earth.csv")
pd.options.display.max_columns = 1000
pd.options.display.max_rows = 5000

df.set_index('Year', inplace = True)
df.drop(['NOAAGlobalTemp uncertainty'], axis = 1, inplace = True)
df_2.set_index('Year', inplace = True)
df_2.drop(['HadCRUT5 uncertainty'], axis = 1, inplace = True)
df_3.set_index('Year', inplace = True)
df_3.drop(['GISTEMP uncertainty'], axis = 1, inplace = True)
df_4.set_index('Year', inplace = True)
df_4.drop(['Berkeley Earth uncertainty'], axis = 1, inplace = True)


plt.plot(df)
plt.plot(df_2)
plt.plot(df_3)
plt.plot(df_4)
plt.title('Global mean temperature difference from 1850 to 1900 (°C)')
plt.legend(['NOAA', 'HadCrUT5', 'GISTEMP', 'Berkeley'])
plt.show()

