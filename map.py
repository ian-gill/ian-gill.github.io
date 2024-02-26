#map.py

import folium

m = folium.Map(location=(19.7216, -155.5),
               zoom_start = 8,
               tiles = 'cartodb positron')

m.save('map.html')

