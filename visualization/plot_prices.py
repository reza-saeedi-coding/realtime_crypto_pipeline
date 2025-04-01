import os
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Load price data from JSON file
def load_price_data(file_path=os.path.join(os.path.dirname(__file__), "..", "data", "crypto_prices.json")):
    if not os.path.exists(file_path):
        print(f"No data file found at {file_path}")
        return []

    with open(file_path, "r") as f:
        try:
            data = json.load(f)
            print("Loaded data:")
            print(data)
            return data
        except json.JSONDecodeError:
            print("Failed to parse JSON.")
            return []

# Extract timestamps and Bitcoin prices from the data
def extract_bitcoin_prices(data):
    timestamps = []
    prices = []

    for entry in data:
        if not isinstance(entry, dict) or entry.get("prices") is None:
            print(f"Skipping bad entry: {entry}")
            continue

        if "bitcoin" not in entry["prices"] or "usd" not in entry["prices"]["bitcoin"]:
            print(f"Skipping incomplete entry: {entry}")
            continue

        try:
            dt = datetime.fromisoformat(entry["timestamp"])
            price = entry["prices"]["bitcoin"]["usd"]

            timestamps.append(dt)
            prices.append(price)

        except Exception as e:
            print(f"Error parsing entry: {e}")

    return timestamps, prices

# Plot the data using matplotlib
def plot_bitcoin_prices(timestamps, prices):
    plt.figure(figsize=(14, 6))
    plt.plot(timestamps, prices, marker="o", linestyle="-", color="blue")

    plt.title("Bitcoin Price Over Time")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")

    # Format x-axis with time
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)

    plt.tight_layout()
    print(f"Plotting {len(timestamps)} data points.")
    plt.show()

# Run if file is executed directly
if __name__ == "__main__":
    data = load_price_data()
    timestamps, prices = extract_bitcoin_prices(data)
    plot_bitcoin_prices(timestamps, prices)
