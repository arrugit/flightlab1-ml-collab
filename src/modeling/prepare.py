from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
import yaml

from src.cleaning import clean_flights

RAW_DATA = Path("data/raw/flight_delays_subset.csv")
PROCESSED_DATA = Path("data/processed")


def main():
    with open("params.yaml", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    delay_threshold = params["data"]["delay_threshold"]
    test_size = params["data"]["test_size"]
    random_state = params["data"]["random_state"]

    # Load raw data
    df = pd.read_csv(RAW_DATA)

    # Clean data and create target
    df = clean_flights(df, delay_threshold=delay_threshold)

    # Features available before the flight
    feature_columns = [
        "Airline",
        "FlightNumber",
        "Origin",
        "Destination",
        "ScheduledDeparture",
        "ScheduledArrival",
        "AircraftType",
        "Distance",
    ]

    X = df[feature_columns].copy()
    y = df["is_delayed"].copy()

    # Convert scheduled timestamps into useful numeric features
    for column in ["ScheduledDeparture", "ScheduledArrival"]:
        X[column] = pd.to_datetime(X[column])
        X[f"{column}_hour"] = X[column].dt.hour
        X[f"{column}_dayofweek"] = X[column].dt.dayofweek

    X = X.drop(columns=["ScheduledDeparture", "ScheduledArrival"])

    # One-hot encode categorical features
    categorical_columns = [
        "Airline",
        "Origin",
        "Destination",
        "AircraftType",
    ]

    X = pd.get_dummies(
        X,
        columns=categorical_columns,
        dtype=int,
    )

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

    X_train.to_csv(PROCESSED_DATA / "X_train.csv", index=False)
    X_test.to_csv(PROCESSED_DATA / "X_test.csv", index=False)
    y_train.to_csv(PROCESSED_DATA / "y_train.csv", index=False)
    y_test.to_csv(PROCESSED_DATA / "y_test.csv", index=False)

    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    print(f"Features: {X_train.shape[1]}")


if __name__ == "__main__":
    main()
