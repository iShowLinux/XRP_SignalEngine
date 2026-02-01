"""

Tired of making bad XRP trades? 
⠀⣠⣶⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⢿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡏⢀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣟⣋⣼⣽⣾⣽⣦⡀⠀⠀⠀
⢀⣼⣿⣷⣾⡽⡄⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⣿⣿⣿⡿⢿⣟⣽⣾⣿⣿⣦⠀⠀
⣸⣿⣿⣾⣿⣿⣮⣤⣤⣤⣤⡀⠀⠀⠻⣿⡯⠽⠿⠛⠛⠩⠩⢿⣿⣿⣿⣿⣷⡀
⣿⣿⢻⣿⣿⣿⣛⡿⠿⠟⠛⠁⣀⣠⣤⣤⣶⣶⣶⣶⣷⣶⠀⠀⠻⣿⣿⣿⣿⣇
⢻⣿⡆⢿⣿⣿⣿⣿⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⣠⣶⣿⣿⣿⣿⡟
⠈⠛⠃⠈⢿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⣠⣾⣿⣿⣿⠟⠋⠁⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠟⡵⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠋⢐⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠁⡖⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠇⡘⡎⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠄⠀


XRP "2-of-3" Long Setup Alert — Upgraded Insight Edition
--------------------------------------------------------
Adds:
✅ Timestamps + cleaner status
✅ Detects when each condition flips True/False (BTC / XRP structure / Momentum)
✅ Prints "WHY" via short reasons + key metrics (levels, lows, breakout state, momentum stats)
✅ Tracks "regime score" changes (0/1/2/3) and explains what changed
✅ Optional alerts: pre-alert on score==1, main alert on score>=2, exit-warning when score drops while “in position”

DATA:
- Coinbase Exchange public candles (no API key)
"""
from config import *
import time
import requests
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict, Any
from datetime import datetime


# =========================
# DATA STRUCTURES
# =========================
@dataclass
class Candle:
    o: float
    h: float
    l: float
    c: float


@dataclass
class XrpStructureState:
    breakout_seen: bool = False
    breakout_index: Optional[int] = None
    pullback_ok: bool = False


@dataclass
class PositionState:
    """
    This script does NOT place trades.
    This state is only for *signal-management*:
    - If you open a position, toggle in_position=True manually or via hotkey later.
    """
    in_position: bool = False
    entered_on_score: Optional[int] = None
    entry_reasons: Optional[List[str]] = None


# =========================
# HELPERS
# =========================
def now_ts() -> str:
    return datetime.now().strftime("%H:%M:%S")


def safe_fmt(x, digits=4) -> str:
    try:
        return f"{float(x):.{digits}f}"
    except Exception:
        return "n/a"


def pct(a: float, b: float) -> float:
    # percent change from b -> a
    if b == 0:
        return 0.0
    return (a - b) / b


def bullets(lines: List[str], indent="  - ") -> str:
    return "\n".join(f"{indent}{ln}" for ln in lines)


# =========================
# FETCH (Coinbase)
# =========================
def fetch_klines_coinbase(product_id: str, granularity: int = 60, limit: int = 200) -> List[Candle]:
    """
    Coinbase returns newest->oldest as:
      [time, low, high, open, close, volume]
    We return oldest->newest.
    """
    url = COINBASE_CANDLES.format(product_id=product_id)
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
    r = requests.get(url, params={"granularity": granularity}, headers=headers, timeout=10)
    r.raise_for_status()

    raw = r.json()
    if not isinstance(raw, list) or not raw:
        raise RuntimeError(f"No candle data for {product_id}")

    candles: List[Candle] = []
    for row in raw[:limit]:
        candles.append(Candle(o=float(row[3]), h=float(row[2]), l=float(row[1]), c=float(row[4])))

    candles.reverse()
    return candles


# =========================
# CONDITIONS
# =========================
def btc_condition(candles: List[Candle]) -> Tuple[bool, Dict[str, Any]]:
    need = BTC_CONTEXT_MINUTES + BTC_HOLD_MINUTES + 2
    if len(candles) < need:
        return False, {"reason": f"need {need} candles, have {len(candles)}"}

    ctx = candles[-BTC_CONTEXT_MINUTES:]
    hold = candles[-BTC_HOLD_MINUTES:]
    prior_window = candles[-(BTC_CONTEXT_MINUTES + BTC_HOLD_MINUTES):-BTC_HOLD_MINUTES]

    level = min(c.l for c in ctx)

    holds_level = all((c.l >= level) and (c.c >= level * (1 + BTC_LEVEL_BUFFER)) for c in hold)

    last_low = min(c.l for c in hold)
    prior_low = min(c.l for c in prior_window)
    no_new_lower_low = last_low >= prior_low

    higher_low = False
    if len(prior_window) >= BTC_HOLD_MINUTES:
        prev15 = prior_window[-BTC_HOLD_MINUTES:]
        higher_low = min(c.l for c in hold) > min(c.l for c in prev15)

    ok = holds_level and no_new_lower_low

    why_true = []
    why_false = []

    if holds_level:
        why_true.append(f"held level ≈ {safe_fmt(level,2)} for {BTC_HOLD_MINUTES}m")
    else:
        why_false.append(f"did not hold level ≈ {safe_fmt(level,2)} for {BTC_HOLD_MINUTES}m")

    if no_new_lower_low:
        why_true.append("no new lower low vs prior window")
    else:
        why_false.append("made a new lower low vs prior window")

    if higher_low:
        why_true.append("higher-low proxy: yes")
    else:
        why_false.append("higher-low proxy: no (optional)")

    details = {
        "level": level,
        "last": candles[-1].c,
        "holds_level": holds_level,
        "no_new_lower_low": no_new_lower_low,
        "higher_low": higher_low,
        "last_low": last_low,
        "prior_low": prior_low,
        "why_true": why_true,
        "why_false": why_false,
    }
    return ok, details


def xrp_structure_condition(candles: List[Candle], state: XrpStructureState) -> Tuple[bool, Dict[str, Any]]:
    if len(candles) < 20:
        return False, {"reason": "not enough candles"}

    lastN = candles[-XRP_HOLD_CANDLES:]
    hold_above = all(c.c > XRP_BREAK_HIGH for c in lastN)

    if not state.breakout_seen and hold_above:
        state.breakout_seen = True
        state.breakout_index = len(candles) - XRP_HOLD_CANDLES
        state.pullback_ok = False

    lowest_since = None
    pullback_ok = False
    still_constructive = candles[-1].c >= XRP_BREAK_LOW

    if state.breakout_seen and state.breakout_index is not None:
        since = candles[state.breakout_index:]
        lowest_since = min(c.l for c in since)
        pullback_ok = lowest_since >= XRP_PULLBACK_FLOOR
        state.pullback_ok = pullback_ok and still_constructive

    ok = state.breakout_seen and state.pullback_ok

    why_true = []
    why_false = []

    if state.breakout_seen:
        why_true.append(f"breakout confirmed: {XRP_HOLD_CANDLES} closes > {XRP_BREAK_HIGH}")
    else:
        why_false.append(f"no breakout yet (need {XRP_HOLD_CANDLES} closes > {XRP_BREAK_HIGH})")

    if state.breakout_seen:
        if lowest_since is not None:
            if pullback_ok:
                why_true.append(f"pullback held floor ≥ {XRP_PULLBACK_FLOOR} (low since breakout {safe_fmt(lowest_since,4)})")
            else:
                why_false.append(f"pullback lost floor {XRP_PULLBACK_FLOOR} (low since breakout {safe_fmt(lowest_since,4)})")

        if still_constructive:
            why_true.append(f"still constructive: last close ≥ {XRP_BREAK_LOW} (last {safe_fmt(candles[-1].c,4)})")
        else:
            why_false.append(f"lost constructive close: last < {XRP_BREAK_LOW} (last {safe_fmt(candles[-1].c,4)})")

    details = {
        "last": candles[-1].c,
        "breakout_seen": state.breakout_seen,
        "breakout_index": state.breakout_index,
        "hold_above_break_high_now": hold_above,
        "lowest_low_since_breakout": lowest_since,
        "pullback_ok": state.pullback_ok,
        "still_constructive": still_constructive,
        "why_true": why_true,
        "why_false": why_false,
    }
    return ok, details


def momentum_condition(candles: List[Candle]) -> Tuple[bool, Dict[str, Any]]:
    """
    CLOSED candle logic:
      c2 = candles[-2] (latest closed candle)
      c1 = candles[-3] (prior closed candle)
    """
    if len(candles) < 5:
        return False, {"reason": "not enough candles"}

    c1 = candles[-3]
    c2 = candles[-2]

    rng = max(c2.h - c2.l, 1e-12)
    body = c2.c - c2.o
    body_pct = abs(body) / rng
    close_loc = (c2.c - c2.l) / rng  # 0..1 (near 1 = near high)

    strong_green = (body > 0) and (body_pct >= STRONG_GREEN_BODY_PCT) and (close_loc >= CLOSE_NEAR_HIGH_PCT)

    follow_through = (c2.c >= c1.c * (1 + FOLLOW_THROUGH_MIN_PCT)) or (c2.c > c1.h)

    ok = strong_green and follow_through

    why_true = []
    why_false = []

    if body > 0:
        why_true.append("green candle")
    else:
        why_false.append("not green candle")

    if body_pct >= STRONG_GREEN_BODY_PCT:
        why_true.append(f"strong body pct {safe_fmt(body_pct,2)} ≥ {STRONG_GREEN_BODY_PCT}")
    else:
        why_false.append(f"weak body pct {safe_fmt(body_pct,2)} < {STRONG_GREEN_BODY_PCT}")

    if close_loc >= CLOSE_NEAR_HIGH_PCT:
        why_true.append(f"close near high {safe_fmt(close_loc,2)} ≥ {CLOSE_NEAR_HIGH_PCT}")
    else:
        why_false.append(f"close not near high {safe_fmt(close_loc,2)} < {CLOSE_NEAR_HIGH_PCT}")

    if follow_through:
        why_true.append("follow-through confirmed")
    else:
        why_false.append("no follow-through")

    details = {
        "c2_open": c2.o,
        "c2_high": c2.h,
        "c2_low": c2.l,
        "c2_close": c2.c,
        "body_pct": body_pct,
        "close_loc": close_loc,
        "follow_through": follow_through,
        "why_true": why_true,
        "why_false": why_false,
    }
    return ok, details


# =========================
# SCORE + CHANGE TRACKING
# =========================
def score_of(btc_ok: bool, xrp_ok: bool, mom_ok: bool) -> int:
    return int(btc_ok) + int(xrp_ok) + int(mom_ok)


def cond_names(btc_ok: bool, xrp_ok: bool, mom_ok: bool) -> List[str]:
    out = []
    if btc_ok:
        out.append("BTC")
    if xrp_ok:
        out.append("XRP_STRUCT")
    if mom_ok:
        out.append("MOM")
    return out


def print_flip(name: str, new_val: bool, details: Dict[str, Any]):
    direction = "✅ TRUE" if new_val else "❌ FALSE"
    print(f"{now_ts()} | {name} flipped -> {direction}")

    if not PRINT_DETAILS_ON_FLIP:
        return

    # show short why lines
    why_key = "why_true" if new_val else "why_false"
    why = details.get(why_key, [])
    if why:
        print(bullets(why))


def alert_box(title: str, lines: List[str]):
    print("\n" + "=" * 90)
    print(f"{now_ts()} | {title}")
    if lines:
        print(bullets(lines))
    print("=" * 90 + "\n")


# =========================
# MAIN LOOP
# =========================
def main():
    xrp_state = XrpStructureState()
    pos = PositionState(in_position=False)

    last_alert_ts = 0
    last_prealert_ts = 0

    prev_flags = {"BTC": None, "XRP_STRUCT": None, "MOM": None}
    prev_score: Optional[int] = None

    while True:
        try:
            btc = fetch_klines_coinbase(BTC_PRODUCT, granularity=GRANULARITY, limit=LIMIT)
            xrp = fetch_klines_coinbase(XRP_PRODUCT, granularity=GRANULARITY, limit=LIMIT)

            btc_ok, btc_info = btc_condition(btc)
            xrp_ok, xrp_info = xrp_structure_condition(xrp, xrp_state)
            mom_ok, mom_info = momentum_condition(xrp)

            score = score_of(btc_ok, xrp_ok, mom_ok)
            active = cond_names(btc_ok, xrp_ok, mom_ok)

            # ---- Detect condition flips ----
            current_flags = {"BTC": btc_ok, "XRP_STRUCT": xrp_ok, "MOM": mom_ok}
            details_map = {"BTC": btc_info, "XRP_STRUCT": xrp_info, "MOM": mom_info}

            for k in ["BTC", "XRP_STRUCT", "MOM"]:
                if prev_flags[k] is None:
                    prev_flags[k] = current_flags[k]
                elif current_flags[k] != prev_flags[k]:
                    print_flip(k, current_flags[k], details_map[k])
                    prev_flags[k] = current_flags[k]

            # ---- Detect score change ----
            if prev_score is None:
                prev_score = score
            elif score != prev_score:
                direction = "↑" if score > prev_score else "↓"
                changed_line = f"score {prev_score} -> {score} {direction} (now true: {', '.join(active) if active else 'none'})"
                print(f"{now_ts()} | {changed_line}")
                prev_score = score

            # ---- Always print a compact status line ----
            print(
                f"{now_ts()} | score={score} | "
                f"BTC={str(btc_ok):5} (last {safe_fmt(btc[-1].c,2)} lvl {safe_fmt(btc_info.get('level'),2)}) | "
                f"XRP={str(xrp_ok):5} (last {safe_fmt(xrp[-1].c,4)}) | "
                f"MOM={str(mom_ok):5}"
            )

            # ---- Pre-alert when exactly 1 condition is true ----
            if PREALERT_ON_SCORE_1 and score == 1:
                if (time.time() - last_prealert_ts) > 60:  # don't spam prealerts
                    which = active[0] if active else "none"
                    lines = [
                        f"Only one filter is true: {which}",
                        "This is context forming, NOT an entry by itself.",
                        "Wait for score>=2 for a higher-quality setup.",
                    ]
                    alert_box("⚠️ Setup forming (score=1)", lines)
                    last_prealert_ts = time.time()

            # ---- Main alert when score >= 2 ----
            if score >= 2 and (time.time() - last_alert_ts) > ALERT_COOLDOWN_SECONDS:
                lines = [
                    f"Conditions TRUE: {', '.join(active)}",
                    f"BTC last {safe_fmt(btc[-1].c,2)} | level {safe_fmt(btc_info.get('level'),2)}",
                    f"XRP last {safe_fmt(xrp[-1].c,4)} | breakout_seen={xrp_info.get('breakout_seen')} pullback_ok={xrp_info.get('pullback_ok')}",
                    f"Momentum: body_pct={safe_fmt(mom_info.get('body_pct'),2)} close_loc={safe_fmt(mom_info.get('close_loc'),2)} follow_through={mom_info.get('follow_through')}",
                    "Reminder: entries are based on score>=2, exits are based on invalidation (structure floor).",
                ]
                alert_box("🚨 XRP LONG SETUP (score>=2)", lines)
                last_alert_ts = time.time()

            # ---- If you are in a position, warn when score drops ----
            # Toggle pos.in_position manually to True when you enter in real life.
            if pos.in_position:
                # Strongest warning: structure invalidation
                if not xrp_ok:
                    # Specifically call out if floor likely broken
                    floor = XRP_PULLBACK_FLOOR
                    last = xrp[-1].c
                    warn_lines = [
                        "You are marked IN POSITION.",
                        "XRP structure filter is now FALSE.",
                        f"Key invalidation zone: floor {floor} and constructive close {XRP_BREAK_LOW}.",
                        f"XRP last: {safe_fmt(last,4)}",
                        "If structure broke, consider reducing risk or exiting (your plan rules).",
                    ]
                    alert_box("🟥 POSITION WARNING: structure no longer valid", warn_lines)

        except Exception as e:
            print(f"{now_ts()} | Error: {e}")

        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
