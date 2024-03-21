from osmapi import OsmApi
import overpy
import json

# Access data for the openstreetmap (OSM) API
OSM_USERNAME = 'SECRETUSERNAME'
OSM_PASSWORD = 'SECRETPASSWORD'

def main():
    # Establish the connection to the OSM API
    api = OsmApi(username=OSM_USERNAME, password=OSM_PASSWORD)

    # Get data from the JSON file
    with open('./data/WES.json', 'r') as file:
        hydrants = json.load(file)

    changeset_id = api.ChangesetCreate({ 'comment': 'Hydranten und Wasserentnahmestellen im Amt Achterwehr hinzugefügt' })
    
    # Add data to OSM
    for hydrant in hydrants:

        checker = overpy.Overpass()
        # Check if hydrant data already exists at the given coordinates
        query = f"""
        [out:json];
        node["emergency"="fire_hydrant"]({float(hydrant['lat']) - 0.0001},{float(hydrant['lon']) - 0.0001},{float(hydrant['lat']) + 0.0001},{float(hydrant['lon']) + 0.0001});
        out body;
        """
        result = checker.query(query)
        if result.nodes:
            print("A fire hydrant already exists at this location.")
        # Add hydrant data to OSM
        else:
            if hydrant['type'] == 'fire_hydrant':
                tags = {'emergency': hydrant['type'], 'fire_hydrant:type': hydrant['subtype']}
                node_id = api.NodeCreate({'lon': float(hydrant['lon']), 'lat': float(hydrant['lat']), 'changeset': changeset_id, 'tag': tags})
                print("Hydrant wurde erfolgreich zu OSM hinzugefügt. Node ID:", node_id)
            else:
                tags = {'emergency': hydrant['type']}
                node_id = api.NodeCreate({'lon': float(hydrant['lon']), 'lat': float(hydrant['lat']), 'changeset': changeset_id, 'tag': tags})
                print("Entnahmestelle wurde erfolgreich zu OSM hinzugefügt. Node ID:", node_id)

    # Close Changeset
    api.ChangesetClose()

if __name__ == "__main__":
    main()

