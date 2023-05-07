import os
import pandas as pd
import fnmatch
import shutil
import numpy as np

directory = 'data/all/street'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    df_temp = pd.read_csv(f)
    year_f = f[len(directory) + 1:len(directory) + 8]
    df_cleaned = df_temp[(df_temp['LSOA name'].str.contains('Barnet')) & (~df_temp['LSOA name'].isna())]
    df_cleaned.to_csv('data/all/street/cleaned/{}-metropolitan-street-cleaned.csv'.format(year_f))