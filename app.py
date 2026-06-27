import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🎯 Sniper Trading Engine")
pair = st.selectbox("Select Pair", ["EURUSD=X", "GBPUSD=X", "BTC-USD"])

if st.button("Generate Signal"):
    ticker = yf.Ticker(pair)
    df = ticker.history(period="10d", interval="1h")
    
    # RSI & Moving Average Logic
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    df['SMA'] = df['Close'].rolling(window=20).mean()
    
    rsi = df['RSI'].iloc[-1]
    price = df['Close'].iloc[-1]
    sma = df['SMA'].iloc[-1]
    
    st.write(f"Price: {price:.5f} | RSI: {rsi:.2f}")
    
    # Advanced Signal
    if rsi < 30 and price > sma:
        st.success("🚀 STRONG BUY")
    elif rsi > 70 and price < sma:
        st.error("📉 STRONG SELL")
    else:
        st.info("⚠️ NEUTRAL - Market trending, waiting for breakout.")
