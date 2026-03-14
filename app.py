import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide")

st.title("TradingView Candlestick")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:

    df = pd.read_excel(file)

    # datetime convert
    df["datetime"] = pd.to_datetime(df["datetime"])

    # sort
    df = df.sort_values("datetime")

    # convert to seconds timestamp
    df["time"] = df["datetime"].apply(lambda x: int(x.timestamp()))

    data = []

    for i in range(len(df)):

        data.append({
            "time": df.iloc[i]["time"],
            "open": float(df.iloc[i]["open"]),
            "high": float(df.iloc[i]["high"]),
            "low": float(df.iloc[i]["low"]),
            "close": float(df.iloc[i]["close"])
        })

    chart = [{
        "chart": {
            "height": 700
        },
        "series": [
            {
                "type": "Candlestick",
                "data": data
            }
        ]
    }]

    renderLightweightCharts(chart)
