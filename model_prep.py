# create new single csv file with all data; aggregate data as well as data already in dataset
# counts for drugs, burglary per lsoa in Barnet, other influencing factors, for each month of every year

import pandas as pd
import os
import re

data_folder = '/volumes/Seagate DNvG/School/dc2/data'

# If the data folder doesn't exist, create it
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

df2010 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2010-crime-data.csv')
df2011 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2011-crime-data.csv')
df2012 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2012-crime-data.csv')
df2013 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2013-crime-data.csv')
df2014 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2014-crime-data.csv')
df2015 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2015-crime-data.csv')
df2016 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2016-crime-data.csv')
df2017 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2017-crime-data.csv')
df2018 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2018-crime-data.csv')
df2019 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2019-crime-data.csv')
df2020 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2020-crime-data.csv')
df2021 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2021-crime-data.csv')
df2022 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2022-crime-data.csv')
df2023 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2023-crime-data.csv')

barnet_df = pd.concat([df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021,
                    df2022, df2023])
barnet_df["Year"] = barnet_df["Month"].str.split("-").str[0]
barnet_df['Month'] = barnet_df['Month'].str[5:]
barnet_df['LSOA name'] = barnet_df['LSOA name'].str.extract('(\d+)', expand=False) # convert lsoa name to just number
# so it's usable in regression
barnet_df['LSOA name'] = barnet_df['LSOA name'].astype(int)

final_df = pd.DataFrame(columns=['Year', 'Month', 'LSOA', 'Burglaries', 'Drugs'])

for year, month, lsoa in sorted(set(zip(barnet_df['Year'].values, barnet_df['Month'].values,
                                        barnet_df['LSOA name'].values))):
    temp_df = barnet_df[(barnet_df['Year'] == year) & (barnet_df['Month'] == month) & (barnet_df['LSOA name'] == lsoa)]
    df_row = pd.Series((year, month, lsoa, temp_df[temp_df['Crime type'] == 'Burglary'].shape[0],
                       temp_df[temp_df['Crime type'] == 'Drugs'].shape[0]), index=['Year', 'Month', 'LSOA',
                                                                                  'Burglaries', 'Drugs'])
    final_df = pd.concat([final_df, pd.DataFrame([df_row])], ignore_index=True)
final_df[['Burglaries', 'Drugs']] = final_df[['Burglaries', 'Drugs']].apply(pd.to_numeric)

output_file = os.path.join(data_folder, 'final_dataset.csv')
final_df.to_csv(output_file, index=False)
