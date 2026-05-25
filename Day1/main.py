import json
from pathlib import Path



user_data = Path("data.json")

with user_data.open(mode="r", encoding="utf-8") as f:
    data = json.load(f)


# create age older than 20 users name list
user_name_list = [user_data["name"] for user_data in data["users"] if user_data["age"] > 20]
print(user_name_list)
