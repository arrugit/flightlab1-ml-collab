import pandas as pd

DATETIME_COLUMNS = [
    "ScheduledDeparture",
    "ActualDeparture",
    "ScheduledArrival",
    "ActualArrival",
]


def clean_flights(df: pd.DataFrame, delay_threshold: int = 15) -> pd.DataFrame:
    """Parse timestamps, drop duplicate flights and add an is_delayed flag."""
    out = df.copy()
    for col in DATETIME_COLUMNS:
        out[col] = pd.to_datetime(out[col])
    out = out.drop_duplicates(subset="FlightID").reset_index(drop=True)
    out["is_delayed"] = (out["DelayMinutes"] >= delay_threshold).astype(int)
    return out
