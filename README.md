
# 🚀 XRP Signal Engine

A **rules-based market condition detector** for XRP traders.

This tool helps identify **low-risk continuation environments** by combining:

- 🟠 **BTC market context**
- 🟢 **XRP price structure**
- 🔵 **Momentum confirmation**

🚫 **This tool does NOT place trades.**  
It is designed to help traders **avoid low-quality conditions** and focus only on periods where **edge exists**.

---

## 🧠 Regime Score Explained

The engine evaluates **three independent conditions** and assigns a **regime score (0–3)** based on how many are true.

| Score | Meaning | Recommended Action |
|------|--------|-------------------|
| **0** | No alignment | Stay out |
| **1** | Context forming | Observe only |
| **2** | Trade-quality setup | Prepare / manage risk |
| **3** | Strong continuation | Highest-quality conditions |

> **Entries are based on score ≥ 2**  
> **Exits are based on price invalidation — not score changes**

---

## 🔍 Conditions Evaluated

### 🟠 1️⃣ BTC Stability (Macro Filter)

BTC acts as the **macro gate**.

BTC is considered *stable* when:
- It holds a price level for **15+ minutes**
- It makes **no new lower low** during that period

This reduces exposure during hostile or unstable market conditions.

---

### 🟢 2️⃣ XRP Structure

XRP must show **constructive bullish structure**:

- Breaks and **holds above 1.600–1.602**
- Pullbacks **hold above 1.595**
- Structure remains intact (no breakdown below the floor)

❌ If structure fails, the trade thesis is invalid.

---

### 🔵 3️⃣ Momentum Confirmation

Momentum confirms **participation**, not just price movement:

- Strong green candle (healthy body size)
- Close near the candle high
- Follow-through candle (no instant rejection)

This helps avoid chasing weak or fading moves.

---

## 🚀 Usage

Run the engine:

```bash
python Engine.py
````

**How to use it in practice:**

1. Run the script
2. Monitor the **regime score**
3. Only consider trades when **score ≥ 2**
4. Always confirm visually on the chart
5. Manage exits based on **structure invalidation**

This tool is a **filter**, not an execution system.

---

# 🛠️ Tuning `config.py` Like a Pro

Your `config.py` is the **control panel** for the signal engine.

The goal is **not** to predict price —
it’s to tune **sensitivity** so alerts match *your trading style*.

### Core principle

* **Engine.py** → rules (rarely changes)
* **config.py** → knobs (changes with volatility + preference)

Use this loop:

> **Observe → Tune one knob → Test → Log → Repeat**

---

## ✅ Step 1 — Choose Your Trading Style

Before touching numbers, decide what you want the engine to be.

### 🟢 Conservative

* Fewer, higher-quality signals
* Willing to miss some moves
* Avoids chop

### 🔴 Aggressive

* Earlier signals
* Accepts more false positives
* Actively manages risk

Document your preference in `config.py` or the README.

---

## ✅ Step 2 — Understand Each Control

### 🟠 BTC Stability (Macro Gate)

```py
BTC_HOLD_MINUTES = 15
BTC_CONTEXT_MINUTES = 30
BTC_LEVEL_BUFFER = 0.0005
```

**What these control**

* `BTC_HOLD_MINUTES` → patience before trusting alts
* `BTC_CONTEXT_MINUTES` → size of recent price context
* `BTC_LEVEL_BUFFER` → strictness of the “hold” (filters micro-wicks)

**How to tune**

* Too many false “stable” signals?
  ➜ Increase `BTC_HOLD_MINUTES` (15 → 20 / 30)
* BTC rarely stabilizes?
  ➜ Decrease `BTC_HOLD_MINUTES` (15 → 10)
* BTC flips too easily?
  ➜ Increase `BTC_LEVEL_BUFFER` (0.0005 → 0.001)

---

### 🟢 XRP Structure (Invalidation System)

```py
XRP_BREAK_LOW = 1.600
XRP_BREAK_HIGH = 1.602
XRP_PULLBACK_FLOOR = 1.595
XRP_HOLD_CANDLES = 3
```

**What these control**

* Breakout zone
* Confirmation strength
* Invalidation floor

**How to tune**

* Breakouts failing instantly?
  ➜ Increase `XRP_HOLD_CANDLES` (3 → 4 / 5)
* Missing moves due to late confirmation?
  ➜ Decrease `XRP_HOLD_CANDLES` (3 → 2)
* Wicky pullbacks but structure holds?
  ➜ Loosen floor slightly (1.595 → 1.594)
* Getting chopped?
  ➜ Tighten floor (1.595 → 1.596)

> **Rule:** Structure levels should reflect *real market structure*, not arbitrary numbers.

---

### 🔵 Momentum (Filters Weak Moves)

```py
STRONG_GREEN_BODY_PCT = 0.45
CLOSE_NEAR_HIGH_PCT = 0.75
FOLLOW_THROUGH_MIN_PCT = 0.0005
```

**What these control**

* Candle quality
* Close strength
* Continuation requirement

**How to tune**

* Momentum almost never triggers?
  ➜ Loosen thresholds:

  * `STRONG_GREEN_BODY_PCT` → 0.40
  * `CLOSE_NEAR_HIGH_PCT` → 0.65
* Too many weak momentum signals?
  ➜ Tighten:

  * `STRONG_GREEN_BODY_PCT` → 0.55
  * `CLOSE_NEAR_HIGH_PCT` → 0.80
* Fake pumps common?
  ➜ Increase follow-through (0.0005 → 0.001)

---

## ✅ Step 3 — Change ONE Thing at a Time

**Bad tuning**

* Changing multiple values at once
* No idea what helped or hurt

**Good tuning**

* Change one knob
* Run 1–2 hours
* Observe behavior
* Keep or revert

---

## ✅ Step 4 — Log Results (Huge Edge)

Keep a simple tuning journal:

* Date / time
* Market condition
* Config change
* Outcome

**Examples**

* “High volatility → `BTC_HOLD_MINUTES=20` reduced false signals”
* “`CLOSE_NEAR_HIGH_PCT=0.80` too strict during ranges”

---

## ✅ Step 5 — Use Presets (Recommended)

Create multiple configs:

* `config_conservative.py` → fewer, higher-quality alerts
* `config_aggressive.py` → earlier, noisier signals

Switch configs without touching the engine.

---

## ⭐ The Golden Rule

> **Don’t tune based on one trade.**
> **Tune based on patterns across many signals.**

The goal is not perfection —
it’s a **repeatable edge filter**.

---

## ⚠️ Disclaimer

Educational use only.
No financial advice.
You are responsible for your own risk management.

```


```
