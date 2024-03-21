import requests
import json

def query_osm_data(query):
    overpass_url = "http://overpass-api.de/api/interpreter"
    response = requests.get(overpass_url, params={"data": query})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error occurred while querying OSM data. Status Code: {response.status_code}")
        return None

def create_feature(lon, lat, tags):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [lon, lat]
        },
        'properties': tags
    }

def extract_features(response):
    features = []
    for element in response.get('elements', []):
        if 'lon' in element and 'lat' in element and 'tags' in element:
            tags = element['tags']
            if 'emergency' in tags:
                if tags['emergency'] in ['fire_hydrant', 'water_tank', 'suction_point']:
                    features.append(create_feature(element['lon'], element['lat'], tags))
    return features

def main():
    # Location on which the search is to be executed.
    location_name = "ORTSNAME"

    query = f"""
    [out:json];
    area["name"="{location_name}"][admin_level=8][boundary="administrative"]->.boundaryarea;
    (
      node(area.boundaryarea)["emergency"="fire_hydrant"];
      node(area.boundaryarea)["emergency"="water_tank"];
      node(area.boundaryarea)["emergency"="suction_point"];
      node(area.boundaryarea)["amenity"="water_point"];
    );
    out center;
    """
    response = query_osm_data(query)
    if response:
        features = extract_features(response)
        if features:
            output = {'type': 'FeatureCollection', 'features': features}
            with open(f'{location_name}_fire_water_data.json', 'w') as f:
                json.dump(output, f, indent=4)
            print("Data successfully extracted and saved.")
        else:
            print("No relevant features found.")
    else:
        print("No response from Overpass API.")

if __name__ == "__main__":
    main()
