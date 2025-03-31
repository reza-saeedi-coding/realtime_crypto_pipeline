import requests

class CryptoDataIngestor:
    def __init__(self, base_url, currencies, vs_currency):
        self.base_url = base_url
        self.currencies = currencies
        self.vs_currency = vs_currency

    def fetch_prices(self):
        endpoint = f"{self.base_url}"
        params = {
            'ids': ','.join(self.currencies),
            'vs_currencies': self.vs_currency
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
