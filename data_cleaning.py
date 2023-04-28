import os
import pandas as pd


# df1 = pd.read_csv('data/2022/2022-01/2022-01-metropolitan-street.csv')
# df2 = pd.read_csv('data/2022/2022-02/2022-02-metropolitan-street.csv')
# df3 = pd.read_csv('data/2022/2022-03/2022-03-metropolitan-street.csv')
# df4 = pd.read_csv('data/2022/2022-04/2022-04-metropolitan-street.csv')
# df5 = pd.read_csv('data/2022/2022-05/2022-05-metropolitan-street.csv')
# df6 = pd.read_csv('data/2022/2022-06/2022-06-metropolitan-street.csv')
# df7 = pd.read_csv('data/2022/2022-07/2022-07-metropolitan-street.csv')
# df8 = pd.read_csv('data/2022/2022-08/2022-08-metropolitan-street.csv')
# df9 = pd.read_csv('data/2022/2022-09/2022-09-metropolitan-street.csv')
# df10 = pd.read_csv('data/2022/2022-10/2022-10-metropolitan-street.csv')
# df11 = pd.read_csv('data/2022/2022-11/2022-11-metropolitan-street.csv')
# df12 = pd.read_csv('data/2022/2022-12/2022-12-metropolitan-street.csv')
# # Combine the monthly dataframes into one
# df2022 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])
#
# # Define the path to the data folder
data_folder = 'data'
#
# If the data folder doesn't exist, create it
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
#
# # Define the path to the output file
# output_file = os.path.join(data_folder, '2022-crime-data.csv')
#
# # Save the DataFrame to a CSV file in the data folder
# df2022.to_csv(output_file, index=False)
#
df1 = pd.read_csv('data/2021/2021-01/2021-01-metropolitan-street.csv')
df2 = pd.read_csv('data/2021/2021-02/2021-02-metropolitan-street.csv')
df3 = pd.read_csv('data/2021/2021-03/2021-03-metropolitan-street.csv')
df4 = pd.read_csv('data/2021/2021-04/2021-04-metropolitan-street.csv')
df5 = pd.read_csv('data/2021/2021-05/2021-05-metropolitan-street.csv')
df6 = pd.read_csv('data/2021/2021-06/2021-06-metropolitan-street.csv')
df7 = pd.read_csv('data/2021/2021-07/2021-07-metropolitan-street.csv')
df8 = pd.read_csv('data/2021/2021-08/2021-08-metropolitan-street.csv')
df9 = pd.read_csv('data/2021/2021-09/2021-09-metropolitan-street.csv')
df10 = pd.read_csv('data/2021/2021-10/2021-10-metropolitan-street.csv')
df11 = pd.read_csv('data/2021/2021-11/2021-11-metropolitan-street.csv')
df12 = pd.read_csv('data/2021/2021-12/2021-12-metropolitan-street.csv')
# Combine the monthly dataframes into one
df2021 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])
output_file = os.path.join(data_folder, '2021-crime-data.csv')

# Save the DataFrame to a CSV file in the data folder
df2021.to_csv(output_file, index=False)

df1 = pd.read_csv('data/2020/2020-01/2020-01-metropolitan-street.csv')
df2 = pd.read_csv('data/2020/2020-02/2020-02-metropolitan-street.csv')
df3 = pd.read_csv('data/2020/2020-03/2020-03-metropolitan-street.csv')
df4 = pd.read_csv('data/2020/2020-04/2020-04-metropolitan-street.csv')
df5 = pd.read_csv('data/2020/2020-05/2020-05-metropolitan-street.csv')
df6 = pd.read_csv('data/2020/2020-06/2020-06-metropolitan-street.csv')
df7 = pd.read_csv('data/2020/2020-07/2020-07-metropolitan-street.csv')
df8 = pd.read_csv('data/2020/2020-08/2020-08-metropolitan-street.csv')
df9 = pd.read_csv('data/2020/2020-09/2020-09-metropolitan-street.csv')
df10 = pd.read_csv('data/2020/2020-10/2020-10-metropolitan-street.csv')
df11 = pd.read_csv('data/2020/2020-11/2020-11-metropolitan-street.csv')
df12 = pd.read_csv('data/2020/2020-12/2020-12-metropolitan-street.csv')
# Combine the monthly dataframes into one
df2020 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])
output_file = os.path.join(data_folder, '2020-crime-data.csv')

# Save the DataFrame to a CSV file in the data folder
df2020.to_csv(output_file, index=False)