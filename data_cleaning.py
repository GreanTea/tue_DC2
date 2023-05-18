import os
import pandas as pd

# # Define the path to the data folder
data_folder = '/volumes/Seagate DNvG/School/dc2/data'
#
# If the data folder doesn't exist, create it
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# data saved on external drive
for year in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]:
    df_dict = {}
    for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        if os.path.exists('{0}/{1}/{1}-{2}/{1}-{2}-metropolitan-street.csv'.format(data_folder, year, month)):
            df_dict['{}-{}'.format(year, month)] = pd.read_csv(
                '{0}/{1}/{1}-{2}/{1}-{2}-metropolitan-street.csv'.format(data_folder, year, month))
        else:
            print("{}-{} doesn't exist".format(year, month)) # test
    df_year = pd.concat(df_dict.values())
    df_year = df_year[df_year['LSOA name'].str.startswith('Barnet', na=False)]
    output_file = os.path.join(data_folder, '{}-crime-data.csv'.format(year))
    df_year.to_csv(output_file, index=False)
