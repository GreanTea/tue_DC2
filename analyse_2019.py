import pandas as pd

#include year before and after to compare
df2018 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2018-crime-data.csv')
df2019 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2019-crime-data.csv')
df2020 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2020-crime-data.csv')

df_all = pd.concat([df2018, df2019, df2020])

df_all["Year"] = df_all["Month"].str.split("-").str[0]
df_all['Month'] = df_all['Month'].str[5:]

barnet_df = df_all[df_all['LSOA name'].str.startswith('Barnet', na=False)]
barnet_df = barnet_df[barnet_df['Crime type'] == 'Burglary']

count_2018 = barnet_df[barnet_df['Year'] == '2018'].shape[0]
count_2019 = barnet_df[barnet_df['Year'] == '2019'].shape[0]
count_2020 = barnet_df[barnet_df['Year'] == '2020'].shape[0]
print('count 2018: {} - 2019: {} - 2020: {}'.format(count_2018, count_2019, count_2020))
# there doesn't seem to be any significant dip in 2019