from operator import index
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ellio\OneDrive\Desktop\Python\CIA.csv", index_col = False)
pd.options.display.max_columns = 1000
pd.options.display.max_rows = 1000

df.drop(['Service', 'Industry', 'Agriculture', 'Coastline (coast/area ratio)', 'Arable (%)', 'Crops (%)', 'Other (%)', 'Region', 'Pop. Density (per sq. mi.)', 'Climate'], axis = 1, inplace = True)
df.set_index('Country', inplace = True)
df = df.dropna()


df_gdp = df.loc[:, 'GDP ($ per capita)']
df_lit = df.loc[:, 'Literacy (%)']

list = list(df.index)

point_size = 1
text_size = 6
plt.scatter(df_gdp, df_lit, s = point_size)


for i, txt in enumerate(list):
    plt.annotate(txt, (df_gdp[i], df_lit[i]), xycoords='data', fontsize = text_size)


plt.xlabel('GDP ($ per capita)')
plt.ylabel('Literacy (%)')
plt.title('Literacy vs GDP')
plt.xscale('log')
plt.show()









