import os
import json
def save_to_json(data, directory="data", filename="crypto_prices.json"):
    """
    Saves the given data to a JSON file in the specified directory.
    Appends new data if file exists, otherwise creates a new file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, filename)

    # 🟡 Step 1: Load existing data if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # 🟢 Step 2: Append new data
    existing_data.append(data)

    # 🔵 Step 3: Save the updated list back to the file
    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=4)
