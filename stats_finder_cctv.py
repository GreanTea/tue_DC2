from statistics import mean

import pandas as pd
from scipy.stats import pearsonr

burg_df = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/final2.csv')  # Load your csv file
burg_df = burg_df[~burg_df['Date'].str.contains('2011')]
burg_df = burg_df.drop(['Date', 'Total'], axis=1)

cctv_df = pd.read_csv('cctv_dist.csv')  # Load your csv file
cctv_df.loc[:, cctv_df.columns != 'Date'] = cctv_df.loc[:, cctv_df.columns != 'Date'].astype(float)
cctv_df = cctv_df[~cctv_df['Date'].str.contains('2011')]
cctv_df = cctv_df.drop(['Date'], axis=1)

# Load your columns
p_list = []
cc_list = []
best_p = 1
best_cc = 0
for column in cctv_df:
    correlation_coefficient, p_value = pearsonr(burg_df[column], cctv_df[column])
    cc_list.append(correlation_coefficient)
    p_list.append(p_value)
    if p_value < best_p:
        best_p = p_value
    if abs(correlation_coefficient) > abs(best_cc):
        best_cc = correlation_coefficient

avg_cc = mean(cc_list)
avg_p = mean(p_list)
worst_p = max(p_list)
temp_abs_cc = [abs(cc) for cc in cc_list]
worst_cc = cc_list[temp_abs_cc.index(min(temp_abs_cc))]
# Print the correlation coefficient and p-value
print("Average Correlation Coefficient: {}".format(avg_cc))
print("Average p-value: {}".format(avg_p))
print("Best Correlation Coefficient: {}".format(best_cc))
print("Best p-value: {}".format(best_p))
print("Worst Correlation Coefficient: {}".format(worst_cc))
print("Worst p-value: {}".format(worst_p))


# Load both dataframes for cctv_dist and burglaries (final2)
# Calculate correlation coefficient and p-value for every LSOA
# return the average, as well as the max-value

# Seems little correlation
# I can maybe try to do it with rows instead of columns, so that it looks at each month, instead of each LSOA separately