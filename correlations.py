import pandas as pd
tree_list = pd.read_csv('/Volumes/Seagate DNvG/School/dc2/data/Borough_tree_list_2021July.csv')
df2021 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2021-crime-data.csv')

# filter on Burglaries
df2021 = df2021[df2021['Crime type'] == 'Burglary']

# for each burrow, find nr_trees in 2021 vs nr_burglaries in 2021
nr_trees_df = pd.DataFrame(columns=['Borough', 'nr_trees', 'burglaries'])
for lsoa in set(df2021['LSOA name']):
    for borough in set(tree_list['borough']):
        if borough == str(lsoa)[:-5]:
            df_row = pd.Series((borough, tree_list[tree_list['borough'] == borough].shape[0],
                                df2021[df2021['LSOA name'].str.startswith(borough, na=False)].shape[0]),
                               index=['Borough', 'nr_trees', 'burglaries'])
            nr_trees_df = pd.concat([nr_trees_df, pd.DataFrame([df_row])], ignore_index=True)
nr_trees_df[['nr_trees', 'burglaries']] = nr_trees_df[['nr_trees', 'burglaries']].apply(pd.to_numeric)

corr_tb = nr_trees_df['nr_trees'].corr(nr_trees_df['burglaries'])
print(corr_tb)