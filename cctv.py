import pandas as pd
import geopandas as gpd
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import chardet

with open('/Users/dennis/Downloads/2017-06-12 CCTV camera list.csv', 'rb') as file:
    cctv = file.read()
encoding = chardet.detect(cctv).get("encoding")
cctv_df = pd.read_csv('/Users/dennis/Downloads/2017-06-12 CCTV camera list.csv', encoding=encoding)
with open('/Users/dennis/Downloads/loc_address.csv', 'rb') as file:
    address = file.read()
encoding2 = chardet.detect(address).get("encoding")
address_df = pd.read_csv('/Users/dennis/Downloads/loc_address.csv', encoding=encoding2)

# convert location to address format
address_list = list()
for line in address_df['Strings'].values:
    if 'Location' in line:
        line = line[1:-1]
        address = line[21:] + ', Barnet, London, United Kingdom'
        address_list.append(address)
cctv_df['Address'] = pd.Series(address_list)

print(cctv_df)
# convert address to longitude and latitude format
locator = Nominatim(user_agent="myGeocoder")
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
cctv_df['geoloc'] = cctv_df['Address'].apply(geocode)
cctv_df['point'] = cctv_df['geoloc'].apply(lambda loc: tuple(loc.point) if loc else None)
cctv_df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(cctv_df['point'].tolist(), index=cctv_df.index)

# Some rows still have empty addresses, so those need to be entered by hand
for i, camera in cctv_df.iterrows():
    if pd.isna(cctv_df.loc[i, 'geoloc']) is True:
        print(camera['Address'])
        cctv_df.at[i, 'latitude'] = str(input("Latitude: "))
        cctv_df.at[i, 'longitude'] = str(input("Longitude: "))
        print(cctv_df.loc[i,])

print(cctv_df)
cctv_df.to_csv('cctv_lonlat.csv')
