from ingestion.crypto_data_ingestor import CryptoDataIngestor
from storage.json_writer import save_to_json
from processing.transformer import add_timestamp
import time

# Configuration
FETCH_COUNT = 500           # Number of price fetches to perform
DELAY_SECONDS = 15          # Time delay between fetches in seconds

# Initialize the ingestor
ingestor = CryptoDataIngestor(
    base_url="https://api.coingecko.com/api/v3/simple/price",
    currencies=["bitcoin", "ethereum"],
    vs_currency="usd"
)

# Main fetch loop
for i in range(FETCH_COUNT):
    print(f"\nFetching prices... ({i + 1}/{FETCH_COUNT})")

    try:
        raw_data = ingestor.fetch_prices()

        if not raw_data:
            print("No valid data received. Skipping this round.")
            time.sleep(DELAY_SECONDS)
            continue

        data_with_timestamp = add_timestamp(raw_data)
        save_to_json(data_with_timestamp)

        print(f"Fetched & saved at {data_with_timestamp['timestamp']}")

    except Exception as e:
        print(f"Error during iteration {i + 1}: {e}")

    time.sleep(DELAY_SECONDS)
