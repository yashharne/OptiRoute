import math
import json
import ast

class utils:
    def haversine(lat1, lon1, lat2, lon2):
        # Radius of the Earth in kilometers
        earth_radius = 6371.0

        # Haversine formula
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Calculate the distance
        distance = earth_radius * c
        return distance*2

    # Function to calculate the total distance of a path
    def total_distance(path):
        dist = 0
        for i in range(len(path) - 1):
            lat1, lon1 = path[i]
            lat2, lon2 = path[i + 1]
            dist += utils.haversine(lat1, lon1, lat2, lon2)
        return dist
    
    def convert_to_dict(json_data):
        shops = json.loads(json_data)

        for shop in shops:
            if 'shops' in shop:
                data_str = shop['shops']
                data_dict = ast.literal_eval(data_str)
                shop['shops'] = data_dict   
        return shops