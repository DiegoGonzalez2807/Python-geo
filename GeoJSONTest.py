import geopandas as gpd

# Ruta al archivo GeoJSON
archivo_geojson = 'New_Scenario_-_Turbine_Coordinates.geojson'

# Leer el archivo GeoJSON
dataframe_geojson = gpd.read_file(archivo_geojson)

print(dataframe_geojson)

#Para sacar la longitud en metros entre dos turbinas
for i in range(len(dataframe_geojson)-1):
    points_df = gpd.GeoDataFrame({'geometry': [dataframe_geojson['geometry'][i], dataframe_geojson['geometry'][i+1]]}, crs='EPSG:4326')
    points_df = points_df.to_crs('EPSG:5234')
    points_df2 = points_df.shift() #We shift the dataframe by 1 to align pnt1 with pnt2
    print(points_df.distance(points_df2))
    #print(dataframe_geojson['geometry'][i].distance(dataframe_geojson['geometry'][i+1]))
