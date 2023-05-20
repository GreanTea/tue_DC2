import itertools

import pandas as pd
import os

data_folder = '/volumes/Seagate DNvG/School/dc2/data'

# If the data folder doesn't exist, create it
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# df2010 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2010-crime-data.csv')
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

barnet_df = pd.concat([df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021,
                       df2022, df2023])
barnet_df['ds'] = barnet_df['Month']
barnet_df["Year"] = barnet_df["Month"].str.split("-").str[0]
barnet_df['Month'] = barnet_df['Month'].str[5:]
columns = ['LSOA', 'Crime'] + sorted(set(barnet_df['ds'].values))
final_df = pd.DataFrame(columns=columns)
# data seems slightly different from HIDEs final.csv
for lsoa in sorted(set(barnet_df['LSOA name'].values)):
    for crime in ['Burglary', 'Drugs']:
        temp_df = barnet_df[(barnet_df['LSOA name'] == lsoa) & (barnet_df['Crime type'] == crime)]
        df_row = pd.Series([lsoa, crime] + [temp_df[temp_df['ds'] == date].shape[0] for date in
                            sorted(set(barnet_df['ds'].values))], index=(['LSOA', 'Crime'] +
                                                                         sorted(set(barnet_df['ds'].values))))
        final_df = pd.concat([final_df, pd.DataFrame([df_row])], ignore_index=True)
output_file = os.path.join(data_folder, 'final2.csv')
final_df.to_csv(output_file, index=False)
