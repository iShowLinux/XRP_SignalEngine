# ===============================
# config_htf_conservative.py
# ===============================
# Purpose:
#   High-confidence, lower-frequency signals for XRP on higher timeframes (1H candles).
#   Best for traders who want fewer alerts and are okay entering later,
#   as long as the setup quality is higher and false positives are reduced.
#
# Best market regime:
#   Base formed and compressing, reclaim attempts possible.
#   You want acceptance above resistance, not mid-range chop.
# ===============================


# --- BTC stability (macro gate) ---------------------------------------------
# BTC_HOLD_MINUTES:
#   Minimum number of minutes BTC must behave "stable" before we trust alt setups.
#   Higher = fewer false positives (more patience). Lower = earlier signals.
BTC_HOLD_MINUTES = 30

# BTC_CONTEXT_MINUTES:
#   How far back we look to define BTC's local "level" and stability context.
#   Higher = smoother / more reliable, but slower to adapt.
BTC_CONTEXT_MINUTES = 120   # was 90 (more smoothing for choppy sessions)

# BTC_LEVEL_BUFFER:
#   Extra cushion above/below the BTC "level" used to avoid micro-wick false flips.
#   Higher = stricter stability requirement.
#   0.0012 = 0.12%
BTC_LEVEL_BUFFER = 0.0012   # was 0.0010


# --- XRP structure (reclaim & invalidation) ----------------------------------
# XRP_BREAK_LOW / XRP_BREAK_HIGH:
#   Breakout / reclaim zone for XRP. Price must break into/above this zone to qualify.
#   Conservative config uses higher reclaim levels to avoid chop.
#
# Tweaked to sit ABOVE the current base/range ceiling (~1.62–1.63),
# so you don't get "long" signals inside the range.
XRP_BREAK_LOW = 1.625        # was 1.635
XRP_BREAK_HIGH = 1.645       # was 1.650

# XRP_PULLBACK_FLOOR:
#   The "structure floor" (invalidation level). If price loses this, the long thesis fails.
#   Set this to a real support zone on your chart (not random).
#
# Tweaked toward the base support area (~1.58–1.59) so minor noise doesn't kill the thesis,
# but a real breakdown does.
XRP_PULLBACK_FLOOR = 1.585   # was 1.610

# XRP_HOLD_CANDLES:
#   Number of *closed* candles that must hold above the breakout zone to count as "accepted".
#   Higher = fewer fake breakouts. Lower = earlier signals.
#
# In a range environment, 2 closes is a strong acceptance filter without being too slow.
XRP_HOLD_CANDLES = 2         # was 3


# --- Momentum confirmation ---------------------------------------------------
# STRONG_GREEN_BODY_PCT:
#   Minimum green candle body size as a fraction of total candle range.
#   Higher = stricter (requires real demand). Lower = more signals.
STRONG_GREEN_BODY_PCT = 0.50  # was 0.45 (ranges lie; require stronger bodies)

# CLOSE_NEAR_HIGH_PCT:
#   How close the close must be to the high, as a fraction of the candle range.
#   Higher = stronger closes (less likely to be rejected).
CLOSE_NEAR_HIGH_PCT = 0.80    # was 0.72 (avoid weak closes that fade)

# FOLLOW_THROUGH_MIN_PCT:
#   Minimum follow-through move after the signal candle.
#   Higher = avoids one-candle pumps, but signals later.
#   0.0012 = 0.12%
FOLLOW_THROUGH_MIN_PCT = 0.0012  # was 0.0010


# --- Runtime / alert behavior ------------------------------------------------
# POLL_SECONDS:
#   How often the script polls for new data.
#   For 1H candles, 60 seconds is plenty.
POLL_SECONDS = 60

# ALERT_COOLDOWN_SECONDS:
#   Minimum time between alerts (prevents spam).
#   Conservative profile uses longer cooldown.
#
# In a choppy base, extend cooldown to reduce repeat alerts.
ALERT_COOLDOWN_SECONDS = 1800  # was 1200 (30 minutes)


# --- Output settings ---------------------------------------------------------
# PREALERT_ON_SCORE_1:
#   If True, prints "setup forming" when exactly 1 of 3 conditions is true.
PREALERT_ON_SCORE_1 = True

# PRINT_DETAILS_ON_FLIP:
#   If True, prints detailed reasoning whenever a condition flips True/False.
PRINT_DETAILS_ON_FLIP = True


# --- Market data source ------------------------------------------------------
# Coinbase product IDs (USD pairs are typically most available)
BTC_PRODUCT = "BTC-USD"
XRP_PRODUCT = "XRP-USD"

# GRANULARITY:
#   Candle size in seconds.
#   3600 = 1-hour candles
GRANULARITY = 3600

# LIMIT:
#   Number of candles fetched from the API each poll.
LIMIT = 200

# Coinbase candles endpoint
COINBASE_CANDLES = "https://api.exchange.coinbase.com/products/{product_id}/candles"