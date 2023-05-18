import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

df_all = pd.concat([df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021,
                    df2022, df2023])
df_all["Year"] = df_all["Month"].str.split("-").str[0]
# Since Year is seperate attribute, it can be removed from the month column
df_all['Month'] = df_all['Month'].str[5:]

# filters on LSOAs that correspond to Barnet
barnet_df = df_all[df_all['LSOA name'].str.startswith('Barnet', na=False)]

burglary_df = barnet_df[barnet_df['Crime type'] == 'Burglary']
drugs_df = barnet_df[barnet_df['Crime type'] == 'Drugs']

burg_drug_ydf = pd.DataFrame(columns=['Year', 'Burglary', 'Drugs'])
for year in sorted(set(barnet_df['Year'].values)):
    df_row = pd.Series((year, burglary_df[burglary_df['Year'] == year].shape[0],
                        drugs_df[drugs_df['Year'] == year].shape[0]), index=['Year', 'Burglary', 'Drugs'])
    burg_drug_ydf = pd.concat([burg_drug_ydf, pd.DataFrame([df_row])], ignore_index=True)
burg_drug_ydf = burg_drug_ydf.apply(pd.to_numeric)
corr_bdy = burg_drug_ydf['Burglary'].corr(burg_drug_ydf['Drugs'])

burg_drug_mdf = pd.DataFrame(columns=['Month', 'Burglary', 'Drugs'])
for month in sorted(set(barnet_df['Month'].values)):
    df_row = pd.Series((month, burglary_df[burglary_df['Month'] == month].shape[0],
                        drugs_df[drugs_df['Month'] == month].shape[0]), index=['Month', 'Burglary', 'Drugs'])
    burg_drug_mdf = pd.concat([burg_drug_mdf, pd.DataFrame([df_row])], ignore_index=True)
burg_drug_mdf = burg_drug_mdf.apply(pd.to_numeric)
corr_bdm = burg_drug_mdf['Burglary'].corr(burg_drug_mdf['Drugs'])

plt.scatter(burg_drug_ydf['Drugs'].values, burg_drug_ydf['Burglary'].values)
plt.xlabel('Drug offenses in Barnet in a year');
plt.ylabel('Burglary offenses in Barnet in a year');
plt.annotate('Correlation = {}'.format(corr_bdy), xy=(100, 2000));
plt.show()

plt.scatter(burg_drug_mdf['Drugs'].values, burg_drug_mdf['Burglary'].values)
plt.xlabel('Drug offenses in Barnet in a month');
plt.ylabel('Burglary offenses in Barnet in a month');
plt.annotate('Correlation = {}'.format(corr_bdm), xy=(725, 4000));
plt.show()