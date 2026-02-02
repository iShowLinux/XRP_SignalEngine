# ===============================
# config_htf_reclaim_trend.py
# Designed for: 1H base -> reclaim -> early trend
# ===============================

# --- BTC stability (HTF confirmation) ---
BTC_HOLD_MINUTES = 20
BTC_CONTEXT_MINUTES = 60
BTC_LEVEL_BUFFER = 0.0008

# --- XRP structure (HTF reclaim) ---
XRP_BREAK_LOW = 1.620
XRP_BREAK_HIGH = 1.635
XRP_PULLBACK_FLOOR = 1.600
XRP_HOLD_CANDLES = 2   # on 1H, 2 closes is meaningful

# --- Momentum (HTF-friendly, not scalp-tight) ---
STRONG_GREEN_BODY_PCT = 0.40
CLOSE_NEAR_HIGH_PCT = 0.68
FOLLOW_THROUGH_MIN_PCT = 0.0007

# --- Runtime / alerts ---
POLL_SECONDS = 60              # 1H chart = slower polling
ALERT_COOLDOWN_SECONDS = 900   # avoid spam

# --- UX ---
PREALERT_ON_SCORE_1 = True
PRINT_DETAILS_ON_FLIP = True

# --- Market ---
BTC_PRODUCT = "BTC-USD"
XRP_PRODUCT = "XRP-USD"

GRANULARITY = 3600   # 1H candles
LIMIT = 200

COINBASE_CANDLES = "https://api.exchange.coinbase.com/products/{product_id}/candles"
