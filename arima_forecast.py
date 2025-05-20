import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from fetch_crypto import fetch_crypto_data  # Import previous script

# Fetch Data
crypto_df = fetch_crypto_data('bitcoin', 'usd', 30)

# Set timestamp as index
crypto_df.set_index('timestamp', inplace=True)

# 1️⃣ Train the ARIMA model
model = ARIMA(crypto_df['price'], order=(5,1,0))  # (p,d,q) values
model_fit = model.fit()

# 2️⃣ Make predictions for the next 7 days
forecast_steps = 7
forecast = model_fit.forecast(steps=forecast_steps)

# 3️⃣ Create a future date range
future_dates = pd.date_range(start=crypto_df.index[-1], periods=forecast_steps+1, freq='D')[1:]

# 4️⃣ Plot the results
plt.figure(figsize=(12,6))
sns.lineplot(data=crypto_df, x=crypto_df.index, y='price', marker='o', color='blue', label="Historical Prices")
sns.lineplot(x=future_dates, y=forecast, marker='o', color='red', label="Predicted Prices")
plt.title("Bitcoin Price Forecast (ARIMA Model)")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.show()

