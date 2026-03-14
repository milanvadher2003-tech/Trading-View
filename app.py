import streamlit as st
import pandas as pd
import json
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("TradingView Style Chart")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:

    df = pd.read_excel(file)

    df.columns = df.columns.str.strip()

    df["datetime"] = pd.to_datetime(df["datetime"])

    df = df.sort_values("datetime")

    # IMPORTANT → ISO format
    df["time"] = df["datetime"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    data = []

    for _, r in df.iterrows():
        data.append({
            "time": r["time"],
            "open": float(r["open"]),
            "high": float(r["high"]),
            "low": float(r["low"]),
            "close": float(r["close"])
        })

    data_json = json.dumps(data)

    html = f"""
    <html>
    <head>
    <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
    </head>

    <body>

    <div id="chart" style="width:100%; height:700px;"></div>

    <script>

    const chart = LightweightCharts.createChart(
        document.getElementById('chart'),
        {{
            layout: {{
                background: {{ color: '#000000' }},
                textColor: '#DDD'
            }},
            grid: {{
                vertLines: {{ color: '#333' }},
                horzLines: {{ color: '#333' }}
            }}
        }}
    );

    const candleSeries = chart.addCandlestickSeries();

    const data = {data_json};

    candleSeries.setData(data);

    chart.timeScale().fitContent();

    </script>

    </body>
    </html>
    """

    components.html(html, height=720)
