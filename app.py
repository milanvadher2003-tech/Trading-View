import streamlit as st
import pandas as pd
import json
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("📊 TradingView Style Candlestick Chart")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime")

    # convert to unix timestamp
    df["time"] = (df["datetime"].astype("int64") // 10**9).astype(int)

    data = []

    for _, row in df.iterrows():
        data.append({
            "time": int(row["time"]),
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"])
        })

    data_json = json.dumps(data)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <script src="https://unpkg.com/lightweight-charts@4.1.1/dist/lightweight-charts.standalone.production.js"></script>
    </head>

    <body>
    <div id="chart" style="width:100%; height:700px;"></div>

    <script>

    const chart = LightweightCharts.createChart(
        document.getElementById('chart'),
        {{
            width: window.innerWidth,
            height: 700,
            layout: {{
                background: {{ color: 'white' }},
                textColor: 'black'
            }},
            grid: {{
                vertLines: {{ color: '#eee' }},
                horzLines: {{ color: '#eee' }}
            }},
            crosshair: {{
                mode: LightweightCharts.CrosshairMode.Normal
            }},
            timeScale: {{
                timeVisible: true
            }}
        }}
    );

    const candleSeries = chart.addCandlestickSeries({{
        upColor: '#008f5a',
        downColor: '#ff6b6b',
        borderVisible: false,
        wickUpColor: '#008f5a',
        wickDownColor: '#ff6b6b'
    }});

    const data = {data_json};

    candleSeries.setData(data);

    chart.timeScale().fitContent();

    </script>
    </body>
    </html>
    """

    components.html(html, height=720)
