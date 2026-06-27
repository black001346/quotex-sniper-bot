import streamlit as st

st.title("🎯 Sniper Trading Engine")

try:
    import yfinance as yf
    import pandas as pd
    
    pair = st.selectbox("Select Currency Pair", ["EURUSD=X", "GBPUSD=X", "BTC-USD"])
    
    if st.button("Generate Signal"):
        ticker = yf.Ticker(pair)
        df = ticker.history(period="5d", interval="1h")
        
        # RSI Calculation
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        current_rsi = df['RSI'].iloc[-1]
        st.write(f"Current RSI: {current_rsi:.2f}")
        
        if current_rsi < 30: st.success("🚀 SIGNAL: BUY")
        elif current_rsi > 70: st.error("📉 SIGNAL: SELL")
        else: st.info("⚠️ SIGNAL: WAIT")
        
except Exception as e:
    st.error("Libraries missing. Please check requirements.")
