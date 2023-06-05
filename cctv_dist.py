import pandas as pd
from numpy import sqrt


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

#
cctv_df = pd.read_csv('cctv_lonlat2.csv')

columns = ['Date'] + sorted(set(barnet_df['LSOA name'].values))
final_df = pd.DataFrame(columns=columns)

for date in sorted(set(barnet_df['ds'].values)):
    dist_list = []
    for lsoa in sorted(set(barnet_df['LSOA name'].values)):
        temp_df = barnet_df[(barnet_df['ds'] == date) & (barnet_df['Crime type'] == 'Burglary') &
                            (barnet_df['LSOA name'] == lsoa)]
        if not temp_df.empty:
            # Calculate the euclidian distance between each burglary and camera for every LSOA per month
            # Then takes the distance to the camera that is closest
            dist = min([sqrt((temp_df.iloc[0]['Longitude'] - cctv_df.loc[i, 'longitude']) ** 2 +
                             (temp_df.iloc[0]['Latitude'] - cctv_df.loc[i, 'latitude']) ** 2)] for i, camera
                       in cctv_df.iterrows())
            dist = float(dist[0])
        else:
            dist = None
        dist_list.append(dist)
    df_row = pd.Series([date] + dist_list,
                       index=(['Date'] + sorted(set(barnet_df['LSOA name'].values))))
    final_df = pd.concat([final_df, pd.DataFrame([df_row])], ignore_index=True)

# Some LSOAs have months with 0 burglaries, so there is no distance to calculate
# These are filled in with the average distance of that particular LSOA
for i, date in final_df.iterrows():
    for column in final_df:
        print(final_df.loc[i,column])
        if pd.isna(final_df.loc[i, column]):
            final_df.at[i, column] = final_df[column].mean(skipna=True)
final_df.to_csv('cctv_dist.csv', index=False)
