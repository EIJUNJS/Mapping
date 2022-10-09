import folium

# create the map of the world
map = folium.Map(location=[38, -90], zoom_start=6, tiles="Stamen Terrain")


map.add_child(folium.Marker(location=[38.1, -90.1], popup="i am marker", icon=folium.Icon('blue')))

map.save("Map1.html")
