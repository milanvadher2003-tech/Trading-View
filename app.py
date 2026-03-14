import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("TradingView Candlestick")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:

    df = pd.read_excel(file)

    # column clean
    df.columns = df.columns.str.strip()

    # datetime convert
    df["datetime"] = pd.to_datetime(df["datetime"])

    # sort
    df = df.sort_values("datetime")

    # unix timestamp
    df["time"] = df["datetime"].apply(lambda x: int(x.timestamp()))

    data = []

    for _, r in df.iterrows():

        data.append({
            "time": int(r["time"]),
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
                    "type": "Candlestick",
                    "data": data
                }
            ]
        }
    ]

    renderLightweightCharts(charts=chart)
