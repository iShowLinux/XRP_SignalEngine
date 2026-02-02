# ===============================
# config_downtrend_protection
# Designed for: heavy sell pressure / lower highs / breakdown risk
# Goal: prevent false "long setup" triggers in a downtrend
# ===============================

BTC_HOLD_MINUTES = 30
BTC_CONTEXT_MINUTES = 60
BTC_LEVEL_BUFFER = 0.0012

XRP_BREAK_LOW = 1.595
XRP_BREAK_HIGH = 1.605
XRP_PULLBACK_FLOOR = 1.575
XRP_HOLD_CANDLES = 5

STRONG_GREEN_BODY_PCT = 0.60
CLOSE_NEAR_HIGH_PCT = 0.85
FOLLOW_THROUGH_MIN_PCT = 0.0012

POLL_SECONDS = 20
ALERT_COOLDOWN_SECONDS = 900

PREALERT_ON_SCORE_1 = True
PRINT_DETAILS_ON_FLIP = True

BTC_PRODUCT = "BTC-USD"
XRP_PRODUCT = "XRP-USD"

GRANULARITY = 60
LIMIT = 200

COINBASE_CANDLES = "https://api.exchange.coinbase.com/products/{product_id}/candles"