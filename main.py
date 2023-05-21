import pandas as pd
import geopandas as gpd
import dash
import plotly.graph_objs as go
import folium
import os
from datetime import datetime
from matplotlib.pyplot import figure
import geopandas as gpd
import requests
import folium
from shapely.geometry import Polygon

now = datetime.now()
fig = figure(figsize=(9, 4), dpi=80)

barnet_gdf = gpd.read_file("https://mapit.mysociety.org/area/2489.geojson")
gdf = gpd.read_file('data/London_Ward.shp')

df2020 = pd.read_csv('data/edited/2020-crime-data.csv')
df2021 = pd.read_csv('data/edited/2021-crime-data.csv')
df2022 = pd.read_csv('data/edited/2022-crime-data.csv')

# print hello



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

#Creating map using requested api from database police that shows ward and population density per ward
#other information can be added later

#list of wards
wards = ['Barnet Vale', 'Brunswich Park', 'Burnt Oak', 'Childs Hill', 'Colindale North', 'Colindale South', 'Cricklewood', 'East Barnet', 'East Finchley', 'Edgware', 'Edgwarebury', 'Finchley Church End', 'Friern Barnet', 'Garden Suburb', 'Golders Green', 'Hendon', 'High Barnet', 'Mill Hill', 'Totteridge and Woodside', 'Underhill', 'West Finchley', 'West Hendon', 'Whetstone', 'Woodhouse']

#list of all ward ids
barnet_ids = []
for d in response.json():
    if d['name'] in wards:
        barnet_ids.append(d['id'])

#df with the id and name of each neighbourhood from requested api data
response = requests.get("https://data.police.uk/api/metropolitan/neighbourhoods")
barnet_df = pd.DataFrame(response.json())
barnet_df = barnet_df[barnet_df['name'].isin(wards)]
barnet_df = barnet_df.set_index('id')
#barnet_df

#requests the boundaries per ward
def bounds(x):
    bound = requests.get(f"https://data.police.uk/api/metropolitan/{x}/boundary").json()
    bound = [(float(d["latitude"]), float(d["longitude"])) for d in bound]
    return bound

barnet_df['boundaries'] = barnet_df.apply(lambda x: bounds(x.name), axis=1)
barnet_df.drop(index='E05013545', inplace=True)

#adding column with population density per ward /km2 based on data of 2021
values = [4.797, 8.584, 6.219, 12.089, 11.900, 5.135, 4.676, 6.590, 3.699, 2.491, 6.306, 6.679, 3.067, 9.345, 6.528, 1.381, 2.347, 1.519, 5.861, 7.908, 5.473, 4.245, 6.771]
barnet_df['population density(/km2)'] = values
#barnet_df

#create map by selecting the boundaries of each ward and plotting a polygon and adding those to a map
m = folium.Map(location=[51.604341, -0.202671], zoom_start=15)
for index, row in barnet_df.iterrows():
    polygon = folium.Polygon(
        locations=row['boundaries'],
        tooltip='Ward name: {} <br>Population Density: {} per km²'.format(row['name'], row['population density(/km2)']),
        color='red',
        fill_color='blue',
        fill_opacity=0.2,
        weight=2,
    )
    polygon.add_to(m)

# Display the map
#m


