import pandas
from geopy.geocoders import ArcGIS

nom = ArcGIS()

df = pandas.read_csv("files/supermarkets.csv")

df["Address"]=df["Address"]+", "+df["City"] + ", "+ df["State"]+ ", " + df["Country"]

df

df["Coordinates"]=df["Address"].apply(nom.geocode)
df
 df.Coordinates[0]
 df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None) 