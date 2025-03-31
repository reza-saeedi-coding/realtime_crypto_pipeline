from datetime import datetime
def add_timestamp(data):
    """
    Adds a current timestamp to the fetched crypto data.
    Returns a new dictionary with 'timestamp' and 'prices'.
    """
    timestamp = datetime.utcnow().isoformat()
    return {
        "timestamp": timestamp,
        "prices": data
    }
