import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fetch_crypto import fetch_crypto_data  # Importing previous script

# Fetch Data
crypto_df = fetch_crypto_data('bitcoin', 'usd', 30)

# 1️⃣ Check for missing values
print("Missing Values:\n", crypto_df.isnull().sum())

# 2️⃣ Remove duplicates (if any)
crypto_df.drop_duplicates(inplace=True)

# 3️⃣ Set 'timestamp' as the index for better visualization
crypto_df.set_index('timestamp', inplace=True)

# Display cleaned data
print("Cleaned Data:\n", crypto_df.head())


# Plotting Bitcoin Price Trend
plt.figure(figsize=(12,6))
sns.lineplot(data=crypto_df, x=crypto_df.index, y='price', marker='o', color='blue')
plt.title("Bitcoin Price Trend (Last 30 Days)")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.grid(True)
plt.xticks(rotation=45)  # Rotate dates for better visibility
plt.show()
