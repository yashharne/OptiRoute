
import itertools
import math

def generateRoute(shops , items_to_visit):
    # Haversine distance function
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
            dist += haversine(lat1, lon1, lat2, lon2)
        return dist


    # Function to find the shortest path visiting unique items
    def tsp_with_items(shops, items_to_visit, start_lat, start_lon):
        # Helper function to recursively find the shortest path with constraints
        def backtrack(current_path, current_distance, visited_items):
            if set(visited_items) == set(items_to_visit):
                # All unique items have been visited
                if current_distance < shortest_distance[0]:
                    shortest_distance[0] = current_distance
                    shortest_path[0] = current_path[:]
                return

            last_visited_coords, _ = current_path[-1]
            for shop in shops:
                shop_coords = (shop['shops']['latitude'], shop['shops']['longitude'])
                if shop_coords not in [coord for coord, _ in current_path] and shop['name'] not in visited_items:
                    # Calculate distance from the last visited node to the current shop
                    new_distance = current_distance + shop['price']+haversine(last_visited_coords[0], last_visited_coords[1], shop_coords[0], shop_coords[1])
                    new_path = current_path + [(shop_coords, shop['name'])]
                    new_visited_items = visited_items + [shop['name']]
                    backtrack(new_path, new_distance, new_visited_items)

        shortest_path = [[]]
        shortest_distance = [float('inf')]
        initial_path = [((start_lat, start_lon), "Start")]
        visited_items = []

        backtrack(initial_path, 0, visited_items)

        return shortest_path[0]

    # Example usage:
    start_lat = 18.46413156  # Starting latitude
    start_lon = 73.83249422  # Starting longitude

    best_path = tsp_with_items(shops, items_to_visit, start_lat, start_lon)
    print("Best path found:")
    for (lat, lon), item in best_path:
        print(f"Latitude: {lat}, Longitude: {lon}, Item: {item}")



# Define the data for shops
shops = [
    {
        "item_id": "it1",
        "name": "milk",
        "price": 18,
        "quantity": 15,
        "shop_id": "S1",
        "shops": {
            "Name": "Chamunda General Stores",
            "id": "S1",
            "latitude": 18.46413156,
            "longitude": 73.83249422
        }
    },
    {
        "item_id": "it2",
        "name": "milk",
        "price": 19,
        "quantity": 10,
        "shop_id": "S2",
        "shops": {
            "Name": "Maharashtra General Store",
            "id": "S2",
            "latitude": 18.46395347,
            "longitude": 73.83244594
        }
    },
    {
        "item_id": "it3",
        "name": "milk",
        "price": 20,
        "quantity": 12,
        "shop_id": "S5",
        "shops": {
            "Name": "SHREE LAKSHMI KIRANA AND GENERAL STORE",
            "id": "S5",
            "latitude": 18.46826159,
            "longitude": 73.82673897
        }
    },
    {
        "item_id": "it7",
        "name": "eggs",
        "price": 6,
        "quantity": 20,
        "shop_id": "S2",
        "shops": {
            "Name": "Maharashtra General Store",
            "id": "S2",
            "latitude": 18.46395347,
            "longitude": 73.83244594
        }
    },
    {
        "item_id": "it8",
        "name": "eggs",
        "price": 6,
        "quantity": 25,
        "shop_id": "S4",
        "shops": {
            "Name": "SHREE DATTA GENERAL STORE",
            "id": "S4",
            "latitude": 18.46781383,
            "longitude": 73.82430352
        }
    },
    {
        "item_id": "it9",
        "name": "eggs",
        "price": 7,
        "quantity": 30,
        "shop_id": "S8",
        "shops": {
            "Name": "Arati Medical And General Stores",
            "id": "S8",
            "latitude": 18.46119719,
            "longitude": 73.83230053
        }
    },
    {
        "item_id": "it10",
        "name": "bread",
        "price": 15,
        "quantity": 10,
        "shop_id": "S9",
        "shops": {
            "Name": "Prasad General Store",
            "id": "S9",
            "latitude": 18.46521133,
            "longitude": 73.84358025
        }
    },
    {
        "item_id": "it11",
        "name": "bread",
        "price": 20,
        "quantity": 12,
        "shop_id": "S8",
        "shops": {
            "Name": "Arati Medical And General Stores",
            "id": "S8",
            "latitude": 18.46119719,
            "longitude": 73.83230053
        }
    },
    {
        "item_id": "it12",
        "name": "bread",
        "price": 15,
        "quantity": 15,
        "shop_id": "S5",
        "shops": {
            "Name": "SHREE LAKSHMI KIRANA AND GENERAL STORE",
            "id": "S5",
            "latitude": 18.46826159,
            "longitude": 73.82673897
        }
    },
    {
        "item_id": "it31",
        "name": "milk",
        "price": 18,
        "quantity": 10,
        "shop_id": "S9",
        "shops": {
            "Name": "Prasad General Store",
            "id": "S9",
            "latitude": 18.46521133,
            "longitude": 73.84358025
        }
    },
    {
        "item_id": "it32",
        "name": "milk",
        "price": 21,
        "quantity": 9,
        "shop_id": "S20",
        "shops": {
            "Name": "Anmol General Store",
            "id": "S20",
            "latitude": 18.44549623,
            "longitude": 73.85999778
        }
    },
    {
        "item_id": "it33",
        "name": "milk",
        "price": 19,
        "quantity": 11,
        "shop_id": "S18",
        "shops": {
            "Name": "Chittranjan General store",
            "id": "S18",
            "latitude": 18.44834107,
            "longitude": 73.87273345
        }
    },
    {
        "item_id": "it37",
        "name": "eggs",
        "price": 8,
        "quantity": 20,
        "shop_id": "S12",
        "shops": {
            "Name": "MAHALAXMI MILKS GENERAL STORES",
            "id": "S12",
            "latitude": 18.45547079,
            "longitude": 73.82779492
        }
    },
    {
        "item_id": "it38",
        "name": "eggs",
        "price": 6,
        "quantity": 18,
        "shop_id": "S14",
        "shops": {
            "Name": "Prathmesh General Stores",
            "id": "S14",
            "latitude": 18.45189162,
            "longitude": 73.84105699
        }
    },
    {
        "item_id": "it39",
        "name": "eggs",
        "price": 5,
        "quantity": 23,
        "shop_id": "S16",
        "shops": {
            "Name": "VIGHNAHARTA GENERAL STORES",
            "id": "S16",
            "latitude": 18.45415972,
            "longitude": 173.837529
        }
    },
    {
        "item_id": "it40",
        "name": "bread",
        "price": 18,
        "quantity": 10,
        "shop_id": "S18",
        "shops": {
            "Name": "Chittranjan General store",
            "id": "S18",
            "latitude": 18.44834107,
            "longitude": 73.87273345
        }
    },
    {
        "item_id": "it41",
        "name": "bread",
        "price": 20,
        "quantity": 8,
        "shop_id": "S19",
        "shops": {
            "Name": "BHARAT GENERAL STORE",
            "id": "S19",
            "latitude": 18.43686535,
            "longitude": 73.86840229
        }
    },
    {
        "item_id": "it42",
        "name": "bread",
        "price": 15,
        "quantity": 9,
        "shop_id": "S20",
        "shops": {
            "Name": "Anmol General Store",
            "id": "S20",
            "latitude": 18.44549623,
            "longitude": 73.85999778
        }
    }
]


# Define the items to visit (unique items)
items_to_visit = ["milk", "eggs", "bread"]

generateRoute(shops , items_to_visit)