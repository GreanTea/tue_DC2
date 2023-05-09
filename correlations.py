import pandas as pd
tree_list = pd.read_csv('/Volumes/Seagate DNvG/School/dc2/data/Borough_tree_list_2021July.csv')
df2021 = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/2021-crime-data.csv')

# filter on Burglaries
df2021 = df2021[df2021['Crime type'] == 'Burglary']

# for each burrow, find nr_trees in 2021 vs nr_burglaries in 2021
nr_trees_dict = {}
for lsoa in set(df2021['LSOA name']):
    for borough in set(tree_list['borough']):
        if borough == str(lsoa)[:-5]:
            nr_trees_dict[borough] = {'nr_trees': tree_list[tree_list['borough'] == borough].shape[0], 'burglaries':
                                    df2021[df2021['LSOA name'].str.startswith(borough, na=False)].shape[0]}
print(nr_trees_dict)