import folium
import os
import json



m = folium.Map(location=[28.3949, 84.1240],tiles="OpenStreetMap",zoom_start=8,min_zoom=7.44)
tooltip='Click for more info'
'''folium.Marker(location=[28.207026,83985162],popup=<i>kaligandaki Hotel</i>,tooltip=tooltip).add_to(m)
folium.CircleMarker(location=[28.207026, 83.985162],
    radius=50,
    popup='Some Other Location',
    fill=True))'''
overlay=os.path.join('overlay.json')

#Underrated Places
folium.Circle(location=[28.278131, 84.309512],
                    radius='500',
                    popup="Ghalegaun",
                    color='red',
                    fill=True,
                    fill_color='aquamarine'    
                    ).add_to(m)
folium.Circle(location=[28.041982, 85.717984],
                    radius='500',
                    popup="Panch Pokhari",
                    color='red',
                    fill=True,
                    fill_color='aquamarine'    
                    ).add_to(m)  
folium.Circle(location=[27.622829, 83.102280],
                    radius='500',
                    popup="Jagdhispur Tal",
                    color='red',
                    fill=True,
                    fill_color='aquamarine'    
                    ).add_to(m)       
folium.Circle(location=[27.575212,83.054484],
                    radius='500',
                    popup="Tilaurakot",
                    color='red',
                    fill=True,
                    fill_color='aquamarine'    
                    ).add_to(m)     
folium.Circle(location=[29.24998,82.250010],
                    radius='6500',
                    popup="Jumla",
                    color='red',
                    fill=True,
                    fill_color='aquamarine'    
                    ).add_to(m)                                     
folium.Marker(location=[27.622829, 83.102280],
    popup='<strong>Jagdhispur Taal</strong>',
    icon=folium.Icon(color='red',icon='info-sign')).add_to(m)
folium.Marker(location=[28.278131, 84.309512],
    popup='<strong>Ghalegaun</strong>',
    icon=folium.Icon(color='red',icon='info-sign')).add_to(m)
folium.Marker(location=[28.041982, 85.717984],
    popup='<strong>Panch Pokhari</strong>',
    icon=folium.Icon(color='red',icon='info-sign')).add_to(m)
folium.Marker(location=[27.575212,83.054484],
    popup='<strong>Tilaurakot</strong>',
    icon=folium.Icon(color='red',icon='info-sign')).add_to(m)

folium.Marker(location=[29.24998,82.250010],
    popup='<strong>Jumla</strong>',
    icon=folium.Icon(color='red',icon='info-sign')).add_to(m)
#Hotels
folium.Marker(location=[27.937790,84.40661],
    popup='<strong>The Old Inn Bandipur<br>(Rural Heritage Pvt.Ltd)</strong>',
    icon=folium.Icon(color='green',icon='info-sign')).add_to(m)    

folium.Marker(location=[28.205604,83.959342],
    popup='<strong>Hotel Iceland</strong>',
    icon=folium.Icon(color='green',icon='info-sign')).add_to(m)

folium.Marker(location=[27.705042,85.342659],
    popup='<strong>The Dwarika Hotel</strong>',
    icon=folium.Icon(color='green',icon='info-sign')).add_to(m)

folium.Marker(location=[27.469446,83.283871],
    popup='<strong>Hotel Little Buddha</strong>',
    icon=folium.Icon(color='green',icon='info-sign')).add_to(m)
folium.Marker(location=[29.274996,82.181713],
    popup='<strong>New Mansarowar Hotel</strong>',
    icon=folium.Icon(color='green',icon='info-sign')).add_to(m)    
'''folium.Marker(location=[],
    popup='<strong></strong>',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(location=[28.215137,83.985643],
    popup='<strong>Hotel Deep Sagar Restaurant & Bar</strong>',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(location=[28.202243,83.9657894],
    popup='<strong></strong>',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(location=[28.203631,83.967345],
    popup='<strong>New Annapurna Guest House</strong>',
    icon=folium.Icon(color='green', icon=logoIcon)
).add_to(m)'''


folium.GeoJson(overlay,name='Pokhara').add_to(m)

m.save('main.html')