import pandas as pd

df2018 = pd.read_csv("data/pp/pp-2018.csv")
df2019 = pd.read_csv("data/pp/pp-2019.csv")
df2020 = pd.read_csv("data/pp/pp-2020.csv")
df2021 = pd.read_csv("data/pp/pp-2021.csv")
df2022 = pd.read_csv("data/pp/pp-2022.csv")

print(df2018.head())