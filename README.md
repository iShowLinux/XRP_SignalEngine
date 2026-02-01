This tool is a rules-based market condition detector for XRP traders. It identifies low-risk
continuation environments
using BTC context, XRP structure, and momentum confirmation. It does NOT place trades.
Regime Score Meaning
0 = No alignment (stay out)
1 = Context forming (observe)
2 = Trade-quality setup (prepare / manage risk)
3 = Strong continuation (highest quality)
Conditions
BTC Stability: BTC holds a level for 15+ minutes and makes no new lower low.
XRP Structure: XRP breaks and holds 1.600–1.602 and pullbacks hold above 1.595.
Momentum: Strong green candle with follow-through, not instant rejection.
Usage
Run the script and wait for score ≥ 2. Always confirm on the chart. Exits are based on structure
invalidation, not score changes.
Disclaimer
Educational use only. No financial advice. You are responsible for risk management
