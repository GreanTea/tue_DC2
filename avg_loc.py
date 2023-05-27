import os
import pandas as pd
import fnmatch
import shutil
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.stats import pearsonr, ttest_ind


df_string = pd.read_csv('data/stringency.csv')
df_string_UK = df_string[df_string['location']=='United Kingdom']
unnecessary = list(df_string_UK.columns)
unnecessary.remove("stringency_index")
unnecessary.remove('date')
df_new = df_string_UK.drop(columns=unnecessary)

df_new['date'] = pd.to_datetime(df_new['date'])

df_first_day=df_new[df_new['date'].dt.is_month_start]

df_first_day['date'] = df_first_day['date'].dt.strftime('%Y-%m')

df_final = pd.read_csv('data/final.csv')

print(df_final)

merged_df = pd.merge(df_final, df_first_day, left_on='ds', right_on='date', how='left')[['ds','y','stringency_index']]

cleaned_df = merged_df.fillna(0)

print(cleaned_df)


t, p = ttest_ind(cleaned_df['y'], cleaned_df['stringency_index'])
print(p)

print(cleaned_df['y'].corr(cleaned_df['stringency_index']))

print(pearsonr(cleaned_df['y'], cleaned_df['stringency_index']))

print(cleaned)