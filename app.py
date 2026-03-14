import streamlit as st
import pandas as pd
import json
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Custom TradingView Chart")

uploaded = st.file_uploader("Upload Excel Data", type=["xlsx"])

if uploaded:

    df = pd.read_excel(uploaded)

    df["datetime"] = pd.to_datetime(df["datetime"])

    data = []

    for _, r in df.iterrows():

        data.append({
            "time": int(r["datetime"].timestamp()),
            "open": float(r["open"]),
            "high": float(r["high"]),
            "low": float(r["low"]),
            "close": float(r["close"]),
            "volume": float(r["volume"])
        })

    json_data = json.dumps(data)

    html = f"""
    <html>

    <head>
    <script src="static/charting_library/charting_library.js"></script>
    </head>

    <body>

    <div id="tv_chart_container" style="height:700px"></div>

    <script>

    const data = {json_data};

    const datafeed = {{

        onReady: (cb) => {{

            setTimeout(() => cb({{
                supported_resolutions: ['1','5','15','60','1D']
            }}), 0);

        }},

        resolveSymbol: (symbol, cb) => {{

            cb({{
                name: symbol,
                type: 'crypto',
                session: '24x7',
                timezone: 'Asia/Kolkata',
                minmov: 1,
                pricescale: 100,
                has_intraday: true,
                supported_resolutions: ['1','5','15','60','1D']
            }});

        }},

        getBars: (symbolInfo, resolution, from, to, onHistoryCallback) => {{

            const bars = data.filter(b => b.time >= from && b.time <= to);

            onHistoryCallback(bars, {{ noData: false }});

        }}

    }};

    new TradingView.widget({{

        container_id: "tv_chart_container",
        autosize: true,
        symbol: "CUSTOM",
        interval: "15",
        datafeed: datafeed,
        library_path: "static/charting_library/",
        locale: "en",
        theme: "dark"

    }});

    </script>

    </body>

    </html>
    """

    components.html(html, height=720)
