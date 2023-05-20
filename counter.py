import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import plotly.express as px
import dash
from dash import dcc, html
import plotly.graph_objs as go
import folium
from folium.plugins import HeatMap
import os
from pathlib import Path
from datetime import datetime
from matplotlib.pyplot import figure

csv_dict= dict()

# assign directory
directory = 'data/all/street/cleaned'

#Iterating over files in directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    #Checking if it is a file
    year_f = f[len(directory)+1:len(directory)+5]
    if os.path.isfile(f):
        if year_f not in csv_dict.keys():
            csv_dict[year_f] = len(pd.read_csv(f))
        else:
            csv_dict[year_f] += len(pd.read_csv(f))
print(csv_dict)

#str='data/all/street\\2010_12-metropolitan-street.csv'
#print(str[16:20])
#print(len(str))
#print(str[len(directory)+1:len(directory)+5])

street_dict = {'2010': 2968, '2011': 40123, '2012': 37516, '2013': 33143, '2014': 31944, '2015': 32044, '2016': 33289, '2017': 33563, '2018': 34751, '2019': 37706, '2020': 41077, '2021': 37459, '2022': 36303, '2023': 5581}
stop_dict = {'2015': 111279, '2016': 146857, '2017': 126924, '2018': 149284, '2019': 265940, '2020': 317505, '2021': 224514, '2022': 167135, '2023': 30041}
outcomes_dict = {'2012': 406151, '2013': 742526, '2014': 645386, '2015': 669400, '2016': 692167, '2017': 555074, '2018': 490952, '2019': 210544, '2020': 706907, '2021': 619145, '2022': 820592, '2023': 305190}
#print(street_dict.keys())
#print(list(street_dict.values()))

f= plt.figure()
plt.bar(list(csv_dict.keys()), list(csv_dict.values()))
f.set_figwidth(10)
plt.xlabel('Year')
plt.ylabel('Amount of burglaries')
plt.title('The amount of burglaries per year in Barnet')
plt.show()