import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)

PROCESSED_DATA = Path("data/processed")
MODEL_PATH = Path("models/model.pkl")
METRICS_PATH = Path("metrics.json")


def main():
    # Load test data
    X_test = pd.read_csv(PROCESSED_DATA / "X_test.csv")
    y_test = pd.read_csv(PROCESSED_DATA / "y_test.csv").squeeze("columns")

    # Load trained model
    model = joblib.load(MODEL_PATH)

    # Generate predictions
    predictions = model.predict(X_test)

    # Calculate metrics
    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
        "f1": f1_score(y_test, predictions, zero_division=0),
    }

    # Save metrics
    with open(METRICS_PATH, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print("Evaluation complete.")
    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")


if __name__ == "__main__":
    main()
