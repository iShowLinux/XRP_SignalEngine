# XRP Signal Engine

A **rules-based market condition detector** for XRP traders.

This tool identifies **low-risk continuation environments** using:
- BTC market context
- XRP price structure
- Momentum confirmation

🚫 **It does NOT place trades.**  
It is designed to help traders avoid low-quality conditions and focus only on periods where **edge exists**.

---

## 🧠 Regime Score Explained

The engine evaluates three independent conditions and assigns a **regime score (0–3)** based on how many are true.

| Score | Meaning | Recommended Action |
|------|--------|-------------------|
| **0** | No alignment | Stay out |
| **1** | Context forming | Observe only |
| **2** | Trade-quality setup | Prepare / manage risk |
| **3** | Strong continuation | Highest-quality conditions |

> **Entries are based on score ≥ 2**  
> **Exits are based on price invalidation, not score changes**

---

## 🔍 Conditions Evaluated

### 1️⃣ BTC Stability (Macro Filter)
BTC is considered stable when:
- It holds a price level for **15+ minutes**
- It makes **no new lower low** during that period

This acts as a macro gate to reduce trading during hostile market conditions.

---

### 2️⃣ XRP Structure
XRP must show constructive bullish structure:
- Breaks and **holds above 1.600–1.602**
- Pullbacks **hold above 1.595**
- Structure remains intact (no breakdown below the floor)

If structure fails, the trade thesis is invalid.

---

### 3️⃣ Momentum Confirmation
Momentum confirms participation, not just price movement:
- Strong green candle (healthy body size)
- Close near the candle high
- Follow-through candle (no instant rejection)

This helps avoid chasing weak or fading moves.

---

## 🚀 Usage

1. Run the script:
   ```bash
   python Engine.py
