#map.py

import folium

m = folium.Map(location=(20.5, -156.75),
               zoom_start = 8,
               tiles = 'cartodb positron')

m.save('map.html')

