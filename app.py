import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("TradingView Chart")

html = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>

  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>

  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": "100%",
  "height": 700,
  "symbol": "BINANCE:BTCUSDT",
  "interval": "15",
  "timezone": "Asia/Kolkata",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_chart"
}
  );
  </script>
</div>
"""

components.html(html, height=720)
