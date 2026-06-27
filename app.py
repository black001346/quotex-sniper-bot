import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Sniper Engine", layout="centered")
st.title("🎯 Sniper Trading Engine")

# Currency pair select karne ka option
pair = st.selectbox("Select Currency Pair", ["EURUSD=X", "GBPUSD=X", "BTC-USD"])

if st.button("Get Live Price"):
    try:
        # Market data fetch karna
        ticker = yf.Ticker(pair)
        data = ticker.history(period="1d")
        
        if not data.empty:
            price = data['Close'].iloc[-1]
            st.success(f"✅ Current Price of {pair}: {price:.5f}")
        else:
            st.error("❌ Data fetch nahi ho saka, market closed ho sakti hai.")
    except Exception as e:
        st.error(f"Error: {e}")
