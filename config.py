# ===============================
# config_trend_continuation_15m.py
# Designed for: 15m trend continuation after reversal
# ===============================

# BTC stability — solid but not overly strict
BTC_HOLD_MINUTES = 20
BTC_CONTEXT_MINUTES = 45
BTC_LEVEL_BUFFER = 0.0008

# XRP structure — trend-based, not range-based
XRP_BREAK_LOW = 1.630
XRP_BREAK_HIGH = 1.640
XRP_PULLBACK_FLOOR = 1.615
XRP_HOLD_CANDLES = 3

# Momentum — healthy impulse, not spike-chasing
STRONG_GREEN_BODY_PCT = 0.48
CLOSE_NEAR_HIGH_PCT = 0.72
FOLLOW_THROUGH_MIN_PCT = 0.0007

# Runtime — slower because 15m timeframe
POLL_SECONDS = 30
ALERT_COOLDOWN_SECONDS = 900

# Alerts / verbosity
PREALERT_ON_SCORE_1 = True
PRINT_DETAILS_ON_FLIP = True

# Products
BTC_PRODUCT = "BTC-USD"
XRP_PRODUCT = "XRP-USD"

# Candle settings
GRANULARITY = 900   # 15-minute candles
LIMIT = 200

COINBASE_CANDLES = "https://api.exchange.coinbase.com/products/{product_id}/candles"
