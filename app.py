import streamlit as st
import yfinance as yf

st.title("🎯 Sniper Trading Engine")

pair = st.selectbox("Select Currency Pair", ["EURUSD=X", "GBPUSD=X", "BTC-USD"])

if st.button("Generate Signal"):
    ticker = yf.Ticker(pair)
    df = ticker.history(period="5d", interval="1h")
    
    # RSI calculation
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    current_rsi = rsi.iloc[-1]
    st.write(f"Current RSI: {current_rsi:.2f}")
    
    if current_rsi < 30: st.success("🚀 SIGNAL: BUY")
    elif current_rsi > 70: st.error("📉 SIGNAL: SELL")
    else: st.info("⚠️ SIGNAL: WAIT")
