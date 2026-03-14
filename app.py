import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("TradingView Style Chart")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:

    df = pd.read_excel(file)

    df["datetime"] = pd.to_datetime(df["datetime"])

    df = df.sort_values("datetime")

    data = []

    for _, r in df.iterrows():

        data.append({
            "time": r["datetime"].strftime("%Y-%m-%d %H:%M:%S"),
            "open": float(r["open"]),
            "high": float(r["high"]),
            "low": float(r["low"]),
            "close": float(r["close"])
        })

    chart = [
        {
            "chart": {
                "height": 700,
                "layout": {
                    "background": {"color": "#000000"},
                    "textColor": "#DDD"
                }
            },
            "series": [
                {
                    "type": "Candlestick",
                    "data": data
                }
            ]
        }
    ]

    renderLightweightCharts(chart, "candlestick")
