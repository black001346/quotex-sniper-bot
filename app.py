import streamlit as st
import yfinance as yf

st.title("🎯 Sniper Trading Engine")
st.write("Engine Online!")

# Currency pair select karne ka option
pair = st.selectbox("Select Currency Pair", ["EURUSD=X", "GBPUSD=X", "BTC-USD"])

# Data fetch karne ka button
if st.button("Get Live Price"):
    data = yf.Ticker(pair)
    price = data.history(period="1d")['Close'].iloc[-1]
    st.write(f"Current Price of {pair}: {price:.5f}")
