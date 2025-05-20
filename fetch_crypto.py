import requests
import pandas as pd

def fetch_crypto_data(crypto_id='bitcoin', currency='usd', days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {'vs_currency': currency, 'days': days, 'interval': 'daily'}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'prices' in data:
        df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp
        return df
    else:
        print("Error fetching data:", data)
        return None

# Example Usage
crypto_df = fetch_crypto_data('bitcoin', 'usd', 30)
print(crypto_df.head())  # Display first few rows

