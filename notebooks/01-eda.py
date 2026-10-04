# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: flightlab (3.12.x)
#     language: python
#     name: python3
# ---

# %%
from pathlib import Path
import sys

ROOT = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
sys.path.insert(0, str(ROOT))

# %%
import pandas as pd

from src.config import RAW_DATA_DIR

df = pd.read_csv(RAW_DATA_DIR / "flight_delays_subset.csv")
df.shape

# %%
from src.cleaning import clean_flights

clean = clean_flights(df)
clean.dtypes

# %%
clean["is_delayed"].value_counts(normalize=True)

# %%
df.head()

# %%
df.info()

# %%
df.isna().sum().sort_values(ascending=False)

# %%
df.describe()

# %%
df.select_dtypes(include="number").hist(figsize=(12, 8), bins=30)

# %% [markdown]
# Leakage warning: ActualDeparture, ActualArrival, DelayReason and DelayMinutes are only known after the flight happens (and DelayReason is empty for 27% of flights, apparently the on-time ones). They must not be used as features when predicting delay. Candidate features are the scheduled times, airline, origin, destination, aircraft type, and distance.
#
