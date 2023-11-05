from flaskr.getDistance import utils
import math
import os
from dotenv import load_dotenv
import pandas as pd

df = pd.read_csv("flaskr/data/data.csv")

items_numppy = df['name'].unique()
items = items_numppy.tolist() + ["Home"]

def find_path_points(start_lat, start_lon):
    shops = utils.convert_to_dict(df.to_json(orient='records'), start_lat, start_lon)
    lst = len(shops)
    
    result, total_dist = optimised_tsp_with_hieuristic(shops, items, start_lat, start_lon, lst)
    print(total_dist)
    print(result)
    
    formatted_best_path = []
    for coord, item, shop in result:
        formatted_coord = {
            "coordinates": {
                "Latitude": coord[0],
                "Longitude": coord[1]
            },
            "Item": item
        }
        formatted_best_path.append(formatted_coord)
    return formatted_best_path
    
def optimised_tsp_with_hieuristic(shops, items_to_visit, start_lat, start_lon, lst):
    
    num_items = len(items_to_visit)      # Calculate the number of unique items to visit
    all_items_mask = (1 << num_items) - 1   # Create a bitmask to represent visited items

    # Helper function to recursively find the shortest path using hieuristics like  A*.
    def dp(mask, last_shop_coord, last_shop_index):
        if  last_shop_index == lst and mask != all_items_mask:
            return float('inf'), []
        if mask == all_items_mask:
            return 0, []  # All unique items have been visited

        if (mask, last_shop_index) in memo:
            return memo[(mask, last_shop_index)]

        shortest_distance = float('inf')
        best_path = []

        for shop_index, shop in enumerate(shops):
            shop_coords = (shop['shops']['latitude'], shop['shops']['longitude'])
            item_name = shop['name']

            if item_name not in items_to_visit:
                continue

            item_index = items_to_visit.index(item_name)

            if not (mask & (1 << item_index)): # If the item hasn't been visited yet
                new_mask = mask | (1 << item_index)
                distance_travel = shop['price'] + utils.haversine(last_shop_coord[0], last_shop_coord[1], shop_coords[0], shop_coords[1])
                dist, path = dp(new_mask, shop_coords, shop_index + 1)

                if dist + distance_travel < shortest_distance:
                    shortest_distance = dist + distance_travel
                    best_path = [(shop_coords, item_name, shop['shops']['Name'])] + path

        if shortest_distance < float('inf'):
            memo[(mask, last_shop_index)] = (shortest_distance, best_path)
            return shortest_distance, best_path
        else:
            return float('inf'), []

    memo = {}
    shortest_distance, shortest_path = dp(0, (start_lat, start_lon), 0)
    
    shortest_path = [((start_lat, start_lon), "Start", "Home")] + shortest_path
    return shortest_path, shortest_distance

