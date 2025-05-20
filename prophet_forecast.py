import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from fetch_crypto import fetch_crypto_data  # Import previous script

# Fetch Data
crypto_df = fetch_crypto_data('bitcoin', 'usd', 30)

# Rename columns for Prophet
crypto_df.rename(columns={'timestamp': 'ds', 'price': 'y'}, inplace=True)

# 1️⃣ Initialize the Prophet model
model = Prophet()
model.fit(crypto_df)

# 2️⃣ Create future dataframe for predictions (Next 7 days)
future = model.make_future_dataframe(periods=7)

# 3️⃣ Make predictions
forecast = model.predict(future)

# 4️⃣ Plot the forecast
fig = model.plot(forecast)
plt.title("Bitcoin Price Forecast (Facebook Prophet)")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.grid(True)
plt.show()

