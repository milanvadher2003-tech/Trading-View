import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("TradingView Candlestick")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:

    df = pd.read_excel(file)

    df.columns = df.columns.str.strip()

    df["datetime"] = pd.to_datetime(df["datetime"])

    df = df.sort_values("datetime")

    df["time"] = df["datetime"].dt.strftime("%Y-%m-%d %H:%M:%S")

    data = []

    for _, r in df.iterrows():

        data.append({
            "time": r["time"],
            "open": float(r["open"]),
            "high": float(r["high"]),
            "low": float(r["low"]),
            "close": float(r["close"])
        })

    chart = [
        {
            "chart": {
                "height": 700
            },
            "series": [
                {
                    "type": "candlestick",
                    "data": data
                }
            ]
        }
    ]

    renderLightweightCharts(chart)
