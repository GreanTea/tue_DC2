import os
import pandas as pd
import fnmatch
import shutil
import numpy as np
from matplotlib import pyplot as plt

directory = 'data/all/street'

data_list = list()

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if not (f == 'data/all/street\\cleaned'):
        df_temp = pd.read_csv(f)
        year_f = f[len(directory) + 1:len(directory) + 8]
        burg_amt = len(df_temp[(df_temp['Crime type']=='Burglary') & (df_temp['LSOA name'].str.contains('Barnet'))])
        drug_amt = len(df_temp[(df_temp['Crime type']=='Drugs') & (df_temp['LSOA name'].str.contains('Barnet'))])
        data_list.append({'filename': year_f,
                         'Amount Burglaries': burg_amt,
                        'Amount Drugs': drug_amt})
results_df = pd.DataFrame(data_list)

print(results_df)

results_df.to_excel('drug_and_burg_count.xlsx')

months = results_df['filename']
burglary_amounts = results_df['Amount Burglaries']
drug_amounts = results_df['Amount Drugs']

plt.bar(months, burglary_amounts, label='Burglaries', width=1, align='edge')
plt.bar(months, drug_amounts, label='Drugs', width=1, align='edge')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Burglaries and Drugs per Month')
plt.legend()
plt.show()