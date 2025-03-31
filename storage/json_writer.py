import json
import os
def save_to_json(data, directory="data", filename="crypto_prices.json"):

    """
    saves the given data to a JSON file in the specifies directory.

    Creates the directory if it doesn't exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        file_path = os.path.join(directory, filename)
        print(file_path)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)