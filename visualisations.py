import pandas as pd
import matplotlib.pyplot as plt

# link for lsoa file: https://geoportal.statistics.gov.uk/datasets/ons::lsoa-dec-2001-ew-bfe/explore
# df_lsoa = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/LSOA_Dec_2001_EW_BFE_2022_8669009712396117932.csv')

df2010 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2010-crime-data.csv')
df2011 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2011-crime-data.csv')
df2012 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2012-crime-data.csv')
df2013 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2012-crime-data.csv')
df2014 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2013-crime-data.csv')
df2015 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2014-crime-data.csv')
df2015 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2015-crime-data.csv')
df2016 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2016-crime-data.csv')
df2017 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2017-crime-data.csv')
df2018 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2018-crime-data.csv')
df2019 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2019-crime-data.csv')
df2020 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2020-crime-data.csv')
df2021 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2021-crime-data.csv')
df2022 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2022-crime-data.csv')
df2023 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2023-crime-data.csv')

df_all = pd.concat([df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021,
                    df2022, df2023])
df_all["Year"] = df_all["Month"].str.split("-").str[0]
# Since Year is seperate attribute, it can be removed from the month column
df_all['Month'] = df_all['Month'].str[5:]

# LSOAs that correspond to Barnet
# barnet_lsoa = df_lsoa[df_lsoa['LSOA01NM'].str.startswith('Barnet', na=False)][['LSOA01CD', 'LSOA01NM']]

# filters on LSOAs that correspond to Barnet
barnet_df = df_all[df_all['LSOA name'].str.startswith('Barnet', na=False)]

# visualise criminal activity per month -- only 2020 and 2021 for now
barnet_mdict = {}
for month in sorted(set(barnet_df['Month'].values)):
    barnet_mdict[month] = barnet_df[barnet_df['Month'] == month].shape[0]

plt.bar(range(len(barnet_mdict)), list(barnet_mdict.values()), tick_label=list(barnet_mdict.keys()))
plt.title('Crimes in Barnet per month');
plt.show()