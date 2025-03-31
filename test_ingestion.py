from ingestion.crypto_data_ingestor import CryptoDataIngestor
from storage.json_writer import save_to_json
from processing.transformer import add_timestamp
import time
ingestor = CryptoDataIngestor(
    base_url="https://api.coingecko.com/api/v3/simple/price",
    currencies=["bitcoin", "ethereum"],
    vs_currency="usd"
)
while True:
    # Fetch raw data
    data = ingestor.fetch_prices()
    print("\nRaw data:")
    print(data)

    # Add timestamp to the data
    processed_data = add_timestamp(data)
    print("\nData with timestamp:")
    print(processed_data)

    # Save processed data
    save_to_json(processed_data)
    print("\nData saved to JSON.")

    # Wait 10 sec before the next fetch
    time.sleep(10)
