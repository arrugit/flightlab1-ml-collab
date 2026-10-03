import pandas as pd

from src.cleaning import DATETIME_COLUMNS, clean_flights


def _sample() -> pd.DataFrame:
    rows = {
        "FlightID": [1, 1, 2, 3],
        "DelayMinutes": [20, 20, 5, 15],
    }
    for col in DATETIME_COLUMNS:
        rows[col] = ["2024-09-01 08:19"] * 4
    return pd.DataFrame(rows)


def test_duplicates_are_dropped():
    assert len(clean_flights(_sample())) == 3


def test_timestamps_are_parsed():
    out = clean_flights(_sample())
    assert pd.api.types.is_datetime64_any_dtype(out["ScheduledDeparture"])


def test_delay_flag_uses_threshold():
    out = clean_flights(_sample(), delay_threshold=15)
    assert out["is_delayed"].tolist() == [1, 0, 1]
