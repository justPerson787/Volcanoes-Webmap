import folium
import pandas #to load csv file with data

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

def marker_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


#create a map object with folium and Leaflet.js

#html for pop-up window on markers
html = """<h4>Volcano information:</h4>
Height: %s m
"""
map = folium.Map(location = [38.58, -99.09],zoom_start=6, tiles = "Mapbox Bright")
feature_group = folium.FeatureGroup(name = 'Map')
for lt, ln, el in zip(lat, lon, elevation):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    feature_group.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), 
    radius = 8, fill_color = marker_color(el), fill_opacity = 0.8, color = 'grey')) 

feature_group.add_child(folium.GeoJson(data = (open('world.json', 'r', encoding = 'utf-8-sig').read())))

map.add_child(feature_group)
map.save("map.html")