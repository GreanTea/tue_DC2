import os
import pandas as pd
import fnmatch
import shutil
import numpy as np
import matplotlib.pyplot as plt

avg_loc = pd.DataFrame()

directory = 'data/all/street/cleaned'

#for filename in os.listdir(directory):
#    f = os.path.join(directory, filename)
#    time_f = f[len(directory)+1:len(directory)+8]
#    df_temp = pd.read_csv(f)
#    if os.path.isfile(f):
#        avg_loc['Longitude'] = df_temp['Longitude'].mean(), df_temp['Latitude'].mean())

# Initialize an empty dataframe to hold the results
data_list = list()

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv') and 'metropolitan-street' in filename:
        filepath = os.path.join(directory, filename)

        # Read in the CSV file as a pandas dataframe
        df = pd.read_csv(filepath)

        # Calculate the average longitude and latitude of the dataframe
        avg_longitude = df['Longitude'].mean()
        avg_latitude = df['Latitude'].mean()

        # Append the results to the results dataframe
        data_list.append({'filename': filename[:7],
                          'avg_longitude': avg_longitude,
                          'avg_latitude': avg_latitude})

results_df = pd.DataFrame(data_list)

results_df.set_index('filename', inplace=True)

cmap = plt.cm.get_cmap('cool', len(os.listdir(directory)))
filenames = list(results_df.index.values)
print(results_df)
fig, ax= plt.subplots()
for i, filename in enumerate(filenames):
    color = cmap(i)
    longitude = results_df.loc[filename, 'avg_longitude']
    latitude = results_df.loc[filename, 'avg_latitude']
    ax.scatter(longitude, latitude, color=color)

    #if i < len(filenames) - 1:
    #    next_filename = filenames[i + 1]
    #    next_longitude = results_df.loc[next_filename, 'avg_longitude']
    #    next_latitude = results_df.loc[next_filename, 'avg_latitude']
    #    ax.plot([longitude, next_longitude], [latitude, next_latitude], color=color)
plt.xlabel('Month')
plt.ylabel('Location')
plt.title('The average location of burglaries per month in Barnet')
plt.show()