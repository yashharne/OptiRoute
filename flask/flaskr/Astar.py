from getDistance import utils
import math
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

#Exampe usage
start_lat = float(os.getenv("start_lat"))  # Starting latitude
start_lon = float(os.getenv("start_lon"))  # Starting longitude

df = pd.read_csv("flaskr/data/data.csv")

items = df['item_id'].unique()
shops = utils.convert_to_dict(df.to_json(orient='records'))


