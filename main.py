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

now = datetime.now()
fig = figure(figsize=(9, 4), dpi=80)

barnet_gdf = gpd.read_file("https://mapit.mysociety.org/area/2489.geojson")
gdf = gpd.read_file('data/London_Ward.shp')

df2020 = pd.read_csv('data/edited/2020-crime-data.csv')
df2021 = pd.read_csv('data/edited/2021-crime-data.csv')
df2022 = pd.read_csv('data/edited/2022-crime-data.csv')



# Combine the dataframes into a single dataframe
df_all = pd.concat([df2020, df2021, df2022])
df_all["Year"] = df_all["Month"].str.split("-").str[0]
# Create a bar chart comparing the number of burglaries across the years
burglary_counts = []
for df in [df2020, df2021, df2022]:
    burglary_counts.append(df[df['Crime type'] == 'Burglary'].shape[0])

data = [go.Bar(x=['2020', '2021', '2022'], y=burglary_counts)]

layout = go.Layout(title='Burglary Occurrences by Year', xaxis_title='Year', yaxis_title='Number of Occurrences')

fig = go.Figure(data=data, layout=layout)



# Count the number of occurrences of each crime type
crime_counts = df2020['Crime type'].value_counts()

# Create a bar chart using Plotly
# fig = px.bar(crime_counts, x=crime_counts.index, y=crime_counts.values)




# df = df122.drop(columns=['Context'])
# df = df122.dropna()

# app = dash.Dash(__name__)
#
# scatter_trace = go.Scattermapbox(
#     lat=df['Latitude'],
#     lon=df['Longitude'],
#     mode='markers',
#     marker=dict(size=10),
#     text=df['Crime type']
# )
#
# # Create the layout for the scatter map on a map
# map_layout = go.Layout(
#     title='My Scatter Map on a Map',
#     autosize=True,
#     hovermode='closest',
#     mapbox=dict(
#         bearing=0,
#         center=dict(
#             lon=-0.2100092790683925, lat=51.61602842377041
#         ),
#         pitch=0,
#         zoom=13
#     )
# )
#
# # Create the figure using the scatter trace and layout
# fig = go.Figure(data=[scatter_trace], layout=map_layout)
#
# # Create the Dash app layout
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


# Print the result
print(fig.show())