import requests
import urllib.parse

# URLs de base
geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"

# TA CLE API
key = "474b61d8-aeaa-4863-828f-78d325bcf13a"

def geocoding(location, key):
    while location == "":
        location = input("Enter the location again: ")

    url = geocode_url + urllib.parse.urlencode({
        "q": location,
        "limit": "1",
        "key": key
    })

    reply = requests.get(url)
    json_data = reply.json()
    status = reply.status_code

    if status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]

        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")

        if state and country:
            new_loc = f"{name}, {state}, {country}"
        elif country:
            new_loc = f"{name}, {country}"
        else:
            new_loc = name

        print(f"Geocoding API URL for {new_loc} (Location Type: {value})")
        print(url)
        return status, lat, lng, new_loc
    else:
        print("Geocode API Error")
        if status != 200:
            print(json_data.get("message", "Unknown error"))
        return status, "null", "null", location


while True:
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Vehicle profiles available on Graphhopper:")
    print("car, bike, foot")
    print("+++++++++++++++++++++++++++++++++++++++++++++")

    vehicle = input("Enter a vehicle profile: ")
    if vehicle in ["q", "quit"]:
        break
    if vehicle not in ["car", "bike", "foot"]:
        print("Invalid vehicle, using car.")
        vehicle = "car"

    loc1 = input("Starting Location: ")
    if loc1 in ["q", "quit"]:
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destination: ")
    if loc2 in ["q", "quit"]:
        break
    dest = geocoding(loc2, key)

    print("=================================================")

    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])

        path_url = route_url + urllib.parse.urlencode({
            "key": key,
            "vehicle": vehicle
        }) + op + dp

        path_reply = requests.get(path_url)
        path_data = path_reply.json()
        status = path_reply.status_code

        print("Routing API Status:", status)
        print("Routing API URL:")
        print(path_url)
        print("=================================================")
        print(f"Directions from {orig[3]} to {dest[3]} by {vehicle}")
        print("=================================================")

        if status == 200:
            distance = path_data["paths"][0]["distance"]
            time_ms = path_data["paths"][0]["time"]

            km = distance / 1000
            miles = km / 1.61

            sec = int(time_ms / 1000 % 60)
            min = int(time_ms / 1000 / 60 % 60)
            hr = int(time_ms / 1000 / 60 / 60)

            print(f"Distance Traveled: {miles:.1f} miles / {km:.1f} km")
            print(f"Trip Duration: {hr:02d}:{min:02d}:{sec:02d}")
            print("=================================================")

            for step in path_data["paths"][0]["instructions"]:
                text = step["text"]
                dist = step["distance"]
                print(f"{text} ( {dist/1000:.1f} km / {dist/1000/1.61:.1f} miles )")

            print("=================================================")
        else:
            print("Error:", path_data.get("message", "Unknown routing error"))
