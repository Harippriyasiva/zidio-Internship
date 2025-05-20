import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from prophet import Prophet

# Set UI Theme & Layout
st.set_page_config(page_title="Crypto Forecasting", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    body { background-color: #f0f2f6; }
    .reportview-container { background-color: #f5f5f5; padding: 20px; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 10px; font-size: 16px; }
    .stDataFrame { border: 2px solid #ddd; padding: 5px; }
    </style>
    """, unsafe_allow_html=True)

# ---- HEADER ----
st.title("📊 Cryptocurrency Time Series Forecasting")
st.write("Track historical trends, analyze forecasts, and get real-time insights.")

# ---- MARKET STATISTICS ----
st.subheader("📊 Market Statistics")

# List of cryptocurrencies to fetch
crypto_list = ["bitcoin", "ethereum", "dogecoin", "solana", "cardano"]
api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_list)}&vs_currencies=usd"

try:
    live_prices = requests.get(api_url).json()
    for coin in crypto_list:
        st.metric(label=f"💰 {coin.capitalize()} Price", value=f"${live_prices[coin]['usd']:.2f}")
except:
    st.error("⚠️ Unable to fetch live prices.")

# ---- TOP-DOWN CONTROL PANEL ----
st.subheader("🔧 Customize Your View")
col1, col2, col3 = st.columns(3)

# User Inputs
crypto = col1.selectbox("Choose Cryptocurrency", ["Bitcoin", "Ethereum", "Dogecoin"])
graph_type = col2.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Statistics", "Moving Average", "Heatmap"])
forecast_days = col3.slider("Forecast Days", 1, 30, 7)

# Button to update graph
if st.button("Generate Forecast"):
    st.success(f"Forecasting for {crypto} over {forecast_days} days...")

# ---- DATA GENERATION ----
dates = pd.date_range("2024-01-01", periods=100)
prices = np.random.randn(100).cumsum() + 50000
forecast_prices = prices + np.random.randn(100) * 200
data = pd.DataFrame({"Date": dates, "Price": prices, "Forecast": forecast_prices})

# ---- CHART DISPLAY ----
import seaborn as sns

if graph_type == "Line Chart":
    st.line_chart(data.set_index("Date")[["Price"]])

elif graph_type == "Bar Chart":
    st.bar_chart(data.set_index("Date")[["Price"]])

elif graph_type == "Statistics":
    st.write(data.describe())

elif graph_type == "Moving Average":
    data["Moving_Avg"] = data["Price"].rolling(window=10).mean()
    st.line_chart(data.set_index("Date")[["Price", "Moving_Avg"]])

elif graph_type == "Heatmap":
    corr = data.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# ---- AI CHATBOT ----
st.subheader("💬 AI Crypto Assistant (Now Predicts!)")

user_query = st.text_input("Ask about crypto trends...")

if user_query:
    # Predict using Prophet
    df = data.rename(columns={"Date": "ds", "Price": "y"})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)  # Predict for 30 days
    forecast = model.predict(future)

    # Get last forecasted value
    predicted_price = forecast["yhat"].iloc[-1]

    # Chatbot Response
    response = f"🤖 AI: {crypto} is expected to reach **${predicted_price:.2f}** in 30 days."
    st.write(response)

# ---- NEWS & ANALYTICS ----
st.subheader("📰 Crypto Market News")
try:
    news_api = "https://api.coingecko.com/api/v3/news"
    response = requests.get(news_api).json()
    for i in range(3):
        st.write(f"🔹 {response[i]['title']}")
except:
    st.error("⚠️ Unable to fetch news.")

st.subheader("📊 Market Analytics")
st.write("🔹 Current Market Sentiment: **Bullish** 📈")
st.write("🔹 24h Volume: **$1.5B**")
st.write("🔹 Dominance: **Bitcoin 45%, Ethereum 25%**")
