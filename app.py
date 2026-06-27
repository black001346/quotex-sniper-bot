import streamlit as st
import yfinance as yf
import pandas_ta as ta

st.title("🎯 Sniper Trading Engine")

pair = st.selectbox("Select Currency Pair", ["EURUSD=X", "GBPUSD=X", "BTC-USD"])

if st.button("Generate Signal"):
    ticker = yf.Ticker(pair)
    df = ticker.history(period="5d", interval="1h")
    
    # RSI Calculation
    df['RSI'] = ta.rsi(df['Close'], length=14)
    current_rsi = df['RSI'].iloc[-1]
    
    st.write(f"Current RSI: {current_rsi:.2f}")
    
    # Signal Logic
    if current_rsi < 30:
        st.success("🚀 SIGNAL: BUY (Oversold)")
    elif current_rsi > 70:
        st.error("📉 SIGNAL: SELL (Overbought)")
    else:
        st.info("⚠️ SIGNAL: WAIT (Neutral)")
