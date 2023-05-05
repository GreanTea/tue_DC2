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
directory = 'data/all/street'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    year_f = f[16:20]
    if os.path.isfile(f):
        if year_f not in csv_dict.keys():
            csv_dict[year_f] = len(pd.read_csv(f))
        else:
            csv_dict[year_f] += len(pd.read_csv(f))
print(csv_dict)

#str='data/all/street\\2010_12-metropolitan-street.csv'
#print(str[16:20])
#print(len(str))

#street: {'2010': 92442, '2011': 1223176, '2012': 1132378, '2013': 1000387, '2014': 948250, '2015': 948265, '2016': 994529, '2017': 1041400, '2018': 1054600, '2019': 1108042, '2020': 1181922, '2021': 1072876, '2022': 1106491, '2023': 170252}
#stop: {'2015': 111279, '2016': 146857, '2017': 126924, '2018': 149284, '2019': 265940, '2020': 317505, '2021': 224514, '2022': 167135, '2023': 30041}
#outcomes: {'2012': 406151, '2013': 742526, '2014': 645386, '2015': 669400, '2016': 692167, '2017': 555074, '2018': 490952, '2019': 210544, '2020': 706907, '2021': 619145, '2022': 820592, '2023': 305190}