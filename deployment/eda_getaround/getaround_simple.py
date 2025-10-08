#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Getaround — simple delay analysis (minimal version)
Usage:
    python getaround_simple.py /path/to/get_around_delay_analysis.xlsx
Outputs:
    - summary.csv  (impact par seuil & scope)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# --------- paramètres rapides ---------
THRESHOLDS = [0, 15, 30, 45, 60, 90, 120, 180, 240]
SCOPES = ["all", "connect_only"]  # "all" ou "connect_only"
# -------------------------------------

if len(sys.argv) < 2:
    print("Usage: python getaround_simple.py /path/to/get_around_delay_analysis.xlsx")
    sys.exit(1)

xlsx_path = Path(sys.argv[1])
if not xlsx_path.exists():
    print(f"Fichier introuvable: {xlsx_path}")
    sys.exit(1)

# 1) Chargement
xls = pd.ExcelFile(xlsx_path)
sheet = "rentals_data" if "rentals_data" in xls.sheet_names else xls.sheet_names[0]
df = pd.read_excel(xls, sheet_name=sheet)
df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_"))

# 2) Cast rapide
for c in ["delay_at_checkout_in_minutes", "time_delta_with_previous_rental_in_minutes", "rental_price"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

if "checkin_type" in df.columns:
    df["checkin_type"] = df["checkin_type"].astype(str).str.lower().str.strip()
if "state" in df.columns:
    df["state"] = df["state"].astype(str).str.lower().str.strip()

# 3) Features minimales
df["gap_to_prev_min"] = df.get("time_delta_with_previous_rental_in_minutes", np.nan)
df["late_prev_min"] = df.get("delay_at_checkout_in_minutes", np.nan)
df["overlap_min"] = (df["late_prev_min"] - df["gap_to_prev_min"]).where(lambda s: s > 0, 0)
df["needed_buffer_min"] = np.maximum(0, df["late_prev_min"] - df["gap_to_prev_min"])
df["revenue_weight"] = df.get("rental_price", pd.Series(1.0, index=df.index)).fillna(0).clip(lower=0)
df["is_connect"] = df.get("checkin_type", "").eq("connect")

# 4) Fonctions ultra-simples
def scope_mask(scope):
    return df["is_connect"] if scope == "connect_only" else pd.Series(True, index=df.index)

def simulate(threshold, scope):
    mask = scope_mask(scope)
    affected = (df["gap_to_prev_min"] < threshold) & df["gap_to_prev_min"].notna()
    affected &= mask

    problems = (df["overlap_min"] > 0) & mask
    solved = problems & (df["needed_buffer_min"] <= threshold)

    total_rev = df.loc[mask, "revenue_weight"].sum()
    affected_rev = df.loc[affected, "revenue_weight"].sum()
    share_rev = (affected_rev / total_rev * 100) if total_rev > 0 else np.nan

    return {
        "scope": scope,
        "threshold_min": threshold,
        "rentals_affected": int(affected.sum()),
        "revenue_share_affected_%": round(share_rev, 2) if pd.notna(share_rev) else np.nan,
        "problems_solved": int(solved.sum()),
        "total_problems_in_scope": int(problems.sum()),
        "solved_rate_%": round((solved.sum()/problems.sum()*100), 2) if problems.sum() else 0.0,
    }

# 5) Boucle et export
rows = [simulate(T, s) for s in SCOPES for T in THRESHOLDS]
summary = pd.DataFrame(rows)
summary.to_csv("summary.csv", index=False)
print("Saved summary.csv")
print(summary.head(10).to_string(index=False))

# 6) Indicateurs d'impact (en un bloc)
impacted = df["overlap_min"] > 0
kpis = {
    "count_impacted": int(impacted.sum()),
    "share_impacted": float((impacted.mean()*100) if len(df) else np.nan),
    "avg_overlap_min": float(df.loc[impacted, "overlap_min"].mean() if impacted.any() else 0.0),
    "p90_overlap_min": float(df.loc[impacted, "overlap_min"].quantile(0.9) if impacted.any() else 0.0),
}
print("Impact KPIs:", kpis)
