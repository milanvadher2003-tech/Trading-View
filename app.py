import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("📊 TradingView Style Candlestick Chart")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime")

    fig = go.Figure(data=[go.Candlestick(
        x=df["datetime"],
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],

        increasing_line_color='#008f5a',
        decreasing_line_color='#ff6b6b'
    )])

    fig.update_layout(

        height=700,

        xaxis_rangeslider_visible=False,

        template="plotly_dark",

        dragmode='pan'
    )

    st.plotly_chart(fig, use_container_width=True)
