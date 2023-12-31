
import itertools
import math
import os
from numbers import Number
from dotenv import load_dotenv
import pandas as pd
import json
import ast
from getDistance import utils

df = pd.read_csv("flaskr/data/data.csv")
items = df['name'].unique()

def find_path_points(start_lat, start_lon):
    shops = utils.convert_to_dict(df.to_json(orient='records'), start_lat, start_lon)

    result = generateRoute(shops, items, start_lat, start_lon)
    print(result)
    
    formatted_best_path = []
    for coord, item in result:
        formatted_coord = {
            "coordinates": {
                "Latitude": coord[0],
                "Longitude": coord[1]
            },
            "Item": item
        }
        formatted_best_path.append(formatted_coord)
    return formatted_best_path

def generateRoute(shops , items_to_visit, start_lat, start_lon):
    # Function to find the shortest path visiting unique items
    def tsp_with_hieuristic(shops, items_to_visit, start_lat, start_lon):
        # Helper function to recursively find the shortest path with constraints
        def backtrack(current_path, current_distance, visited_items):
            if set(visited_items) == set(items_to_visit):
                # All unique items have been visited
                if current_distance < shortest_distance[0]:
                    shortest_distance[0] = current_distance
                    shortest_path[0] = current_path[:]
                return

            last_visited_coords, _, __ = current_path[-1]
            for shop in shops:
                shop_coords = (shop['shops']['latitude'], shop['shops']['longitude'])
                if shop_coords not in [coord for coord, _ ,__ in current_path] and shop['name'] not in visited_items:
                    # Calculate distance from the last visited node to the current shop
                    new_distance = current_distance + shop['price']+utils.haversine(last_visited_coords[0], last_visited_coords[1], shop_coords[0], shop_coords[1])
                    new_path = current_path + [(shop_coords, shop['name'], shop['shops']['Name'])]
                    new_visited_items = visited_items + [shop['name']]
                    # print(new_path)
                    backtrack(new_path, new_distance, new_visited_items)

        shortest_path = [[]]
        shortest_distance = [float('inf')]
        initial_path = [((start_lat, start_lon), "Start", "Home")]
        visited_items = []

        backtrack(initial_path, 0, visited_items)

        return shortest_path[0]

    best_path = tsp_with_hieuristic(shops, items_to_visit, start_lat, start_lon)
    return best_path