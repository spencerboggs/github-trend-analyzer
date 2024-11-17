# reset trending_data.json
import json
import os

JSON_FILE = "trending_data.json"

def clear_data():
    with open(JSON_FILE, "w") as f:
        json.dump([], f)
    print("Data cleared")