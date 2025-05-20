from fetch_crypto import fetch_crypto_data

# Fetch data
crypto_df = fetch_crypto_data('bitcoin', 'usd', 30)

# Check if data exists
if crypto_df is not None and not crypto_df.empty:
    print("✅ Data fetched successfully!")
    print(crypto_df.head())  # Show first 5 rows
else:
    print("❌ No data available. Check API or internet connection.")
