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

from shapely.geometry import Point, Polygon
from tqdm import tqdm
import math
import ast

#df_street_burglary_barnet = pd.read_csv('data/all/street/cleaned/2011-02-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_2 = pd.read_csv('data/all/street/cleaned/2011-03-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_3 = pd.read_csv('data/all/street/cleaned/2011-04-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_4 = pd.read_csv('data/all/street/cleaned/2011-05-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_5 = pd.read_csv('data/all/street/cleaned/2011-06-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_6 = pd.read_csv('data/all/street/cleaned/2011-07-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_7 = pd.read_csv('data/all/street/cleaned/2011-08-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_8 = pd.read_csv('data/all/street/cleaned/2011-09-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_9 = pd.read_csv('data/all/street/cleaned/2011-10-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_10 = pd.read_csv('data/all/street/cleaned/2011-11-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_11 = pd.read_csv('data/all/street/cleaned/2011-12-metropolitan-street-cleaned.csv')
#df_street_burglary_barnet_12 = pd.read_csv('data/all/street/cleaned/2012-01-metropolitan-street-cleaned.csv')


#df_boundaries = pd.read_csv('data/boundary dataframe.csv')

#coordinates = []
#for i in range(len(df_boundaries)):
#    coordinates.append((df_boundaries.loc[i,'name'], ast.literal_eval(df_boundaries.loc[i,'boundaries'])))

#print(coordinates)
#df_list = [df_street_burglary_barnet, df_street_burglary_barnet_2, df_street_burglary_barnet_3, df_street_burglary_barnet_4, df_street_burglary_barnet_5, df_street_burglary_barnet_6, df_street_burglary_barnet_7, df_street_burglary_barnet_8, df_street_burglary_barnet_9, df_street_burglary_barnet_10, df_street_burglary_barnet_11, df_street_burglary_barnet_12]
#lsoa_coords = dict()
#for df in df_list:
 #   for i in range(len(df)):
  #      if not df.loc[i,'LSOA name'] in lsoa_coords.keys():
   #         lsoa_coords[df.loc[i,'LSOA name']] = (df.loc[i,'Latitude'], df.loc[i,'Longitude'])

#print(len(lsoa_coords))
# based on the coordiante of the burglary, find the neighbourhood it belongs to

#ward = dict()
#for name in df_boundaries['name'].values:
#    ward[name]=[]

#ward['Brunswick Park']=[]
#missing = []

#for i in lsoa_coords.keys():
#
 #   point = Point(lsoa_coords[i])
#
 #   for name, coordinate in coordinates:
  #      polygon = Polygon(coordinate)
   #     if not name == None:
    #        if polygon.contains(point):
     #           ward[name] += [i]
      #          break
#
 #           if name == 'Woodhouse' and polygon.contains(point) == False:
  #              ward['Brunswick Park'] += [i]
   #             break

#print(ward)
#flat_lsoa = [(item) for sublist in list(ward.values()) for item in sublist]
#print(len(flat_lsoa))

df_final = pd.read_csv('data/final.csv')

ward = {'Barnet Vale': ['Barnet 002B', 'Barnet 002C', 'Barnet 002D', 'Barnet 005A', 'Barnet 005B', 'Barnet 005C', 'Barnet 005D', 'Barnet 008A', 'Barnet 002E', 'Barnet 004C'], 'Burnt Oak': ['Barnet 021A', 'Barnet 021C', 'Barnet 021E', 'Barnet 024A', 'Barnet 024B', 'Barnet 024D', 'Barnet 024C', 'Barnet 024F', 'Barnet 018D', 'Barnet 021B'], 'Childs Hill': ['Barnet 037A', 'Barnet 038A', 'Barnet 038B', 'Barnet 038C', 'Barnet 038D', 'Barnet 040A', 'Barnet 041B', 'Barnet 041C', 'Barnet 038E', 'Barnet 041A'], 'Colindale North': ['Barnet 024E', 'Barnet 026C', 'Barnet 026D', 'Barnet 026E', 'Barnet 030D', 'Barnet 026A', 'Barnet 026B'], 'Colindale South': ['Barnet 030A', 'Barnet 030E', 'Barnet 030F', 'Barnet 030B'], 'Cricklewood': ['Barnet 039A', 'Barnet 039C', 'Barnet 040B', 'Barnet 040C', 'Barnet 040D', 'Barnet 041D'], 'East Barnet': ['Barnet 003A', 'Barnet 003B', 'Barnet 003C', 'Barnet 003D', 'Barnet 006A', 'Barnet 006B', 'Barnet 006C', 'Barnet 006D', 'Barnet 006E', 'Barnet 002A'], 'East Finchley': ['Barnet 027A', 'Barnet 027B', 'Barnet 029A', 'Barnet 029C', 'Barnet 029E', 'Barnet 033A', 'Barnet 029B', 'Barnet 029D', 'Barnet 027C', 'Barnet 029F'], 'Edgware': ['Barnet 013F', 'Barnet 014D', 'Barnet 014E', 'Barnet 014F', 'Barnet 018A', 'Barnet 018C', 'Barnet 018E', 'Barnet 021D', 'Barnet 018B', 'Barnet 013E'], 'Edgwarebury': ['Barnet 007A', 'Barnet 013A', 'Barnet 013B', 'Barnet 013C', 'Barnet 013D', 'Barnet 014B', 'Barnet 014C', 'Barnet 014A'], 'Finchley Church End': ['Barnet 020E', 'Barnet 023C', 'Barnet 025A', 'Barnet 025B', 'Barnet 025C', 'Barnet 028A', 'Barnet 028B', 'Barnet 028C', 'Barnet 028D', 'Barnet 028E', 'Barnet 023A'], 'Friern Barnet': ['Barnet 011A', 'Barnet 015A', 'Barnet 015B', 'Barnet 015C', 'Barnet 015D', 'Barnet 015E', 'Barnet 022C', 'Barnet 022D', 'Barnet 022E', 'Barnet 022A', 'Barnet 022B'], 'Garden Suburb': ['Barnet 033B', 'Barnet 033C', 'Barnet 033D', 'Barnet 033E', 'Barnet 033F', 'Barnet 035A', 'Barnet 035B'], 'Golders Green': ['Barnet 035C', 'Barnet 035D', 'Barnet 035E', 'Barnet 035F', 'Barnet 037B', 'Barnet 037C', 'Barnet 037D', 'Barnet 037E', 'Barnet 037F', 'Barnet 039B'], 'Hendon': ['Barnet 031A', 'Barnet 031B', 'Barnet 032A', 'Barnet 032B', 'Barnet 032C', 'Barnet 032D', 'Barnet 032E', 'Barnet 034A', 'Barnet 034B', 'Barnet 034C', 'Barnet 034D', 'Barnet 031C'], 'High Barnet': ['Barnet 001A', 'Barnet 001C', 'Barnet 001D', 'Barnet 007B', 'Barnet 007F', 'Barnet 001B', 'Barnet 007E', 'Barnet 001F'], 'Mill Hill': ['Barnet 016A', 'Barnet 016C', 'Barnet 016D', 'Barnet 017A', 'Barnet 017B', 'Barnet 017C', 'Barnet 025D', 'Barnet 025E', 'Barnet 016B'], 'Totteridge and Woodside': ['Barnet 007C', 'Barnet 007D', 'Barnet 012B', 'Barnet 012C', 'Barnet 017D', 'Barnet 020A', 'Barnet 020B', 'Barnet 019B', 'Barnet 012A'], 'Underhill': ['Barnet 004B', 'Barnet 004D', 'Barnet 004E', 'Barnet 001E', 'Barnet 004A', 'Barnet 004F'], 'West Finchley': ['Barnet 019A', 'Barnet 019D', 'Barnet 020D', 'Barnet 023B', 'Barnet 023D', 'Barnet 027E', 'Barnet 027F', 'Barnet 020C', 'Barnet 027D', 'Barnet 019C'], 'West Hendon': ['Barnet 032F', 'Barnet 036A', 'Barnet 036B', 'Barnet 036C', 'Barnet 036D', 'Barnet 036F', 'Barnet 039D', 'Barnet 031D', 'Barnet 036E'], 'Whetstone': ['Barnet 008B', 'Barnet 008C', 'Barnet 008D', 'Barnet 008E', 'Barnet 011B', 'Barnet 012D', 'Barnet 011C'], 'Woodhouse': ['Barnet 011D', 'Barnet 011E', 'Barnet 012E', 'Barnet 015F', 'Barnet 019E', 'Barnet 019F', 'Barnet 022F'], 'Brunswick Park': ['Barnet 009B', 'Barnet 009C', 'Barnet 009D', 'Barnet 009E', 'Barnet 010A', 'Barnet 010B', 'Barnet 010C', 'Barnet 010D', 'Barnet 010E', 'Barnet 009A']}
a = ['ds', 'Year', 'Month', 'y']
a.extend(list(ward.keys()))
print(a)
df_final_ward = pd.DataFrame(columns=a)

for column in df_final.columns.values:
    if column in ['ds', 'Year', 'Month', 'y']:
        df_final_ward[column] = df_final[column]
    else:
        for wrd in ward.keys():
            if column in ward[wrd]:
                print(column, wrd)
#                if df_final_ward.loc[1, wrd].isnull:
#                    df_final_ward[wrd] = df_final[column]
#                else:
                print(df_final_ward.loc[1,wrd])
                if math.isnan(df_final_ward.loc[1,wrd]):
                    df_final_ward[wrd] = df_final[column]
                else:
                    df_final_ward[wrd] += df_final[column]
print(df_final_ward)

df_final_ward.to_csv('final_ward.csv')