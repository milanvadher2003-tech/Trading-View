import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("TradingView Style Candlestick")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:

    df = pd.read_excel(file)

    # clean columns
    df.columns = df.columns.str.strip()

    # datetime convert
    df["datetime"] = pd.to_datetime(df["datetime"])

    # sort
    df = df.sort_values("datetime")

    # convert to ISO format
    df["time"] = df["datetime"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    data = []

    for _, r in df.iterrows():

        data.append({
            "time": str(r["time"]),
            "open": float(r["open"]),
            "high": float(r["high"]),
            "low": float(r["low"]),
            "close": float(r["close"])
        })

    chart = [{
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
    }]

    renderLightweightCharts(chart)
