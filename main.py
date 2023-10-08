from fastapi import FastAPI
import geojson

app = FastAPI()

# Lee el archivo GeoJSON
with open("dalas_PM25.geojson", "r") as f:
    geojson_data = geojson.load(f)

@app.get("/")
async def get_geojson():
    return geojson_data
