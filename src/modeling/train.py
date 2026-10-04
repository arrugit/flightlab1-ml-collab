from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import yaml

PROCESSED_DATA = Path("data/processed")
MODEL_DIR = Path("models")


def main():
    with open("params.yaml", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    model_params = params["model"]

    # Load prepared training data
    X_train = pd.read_csv(PROCESSED_DATA / "X_train.csv")
    y_train = pd.read_csv(PROCESSED_DATA / "y_train.csv").squeeze("columns")

    # Create model
    model = RandomForestClassifier(
        n_estimators=model_params["n_estimators"],
        max_depth=model_params["max_depth"],
        min_samples_leaf=model_params["min_samples_leaf"],
        random_state=model_params["random_state"],
        n_jobs=-1,
        class_weight="balanced",
    )

    # Train
    model.fit(X_train, y_train)

    # Save model
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_DIR / "model.pkl")

    print("Model training complete.")
    print(f"Training samples: {len(X_train)}")
    print(f"Features: {X_train.shape[1]}")
    print(f"Model saved to: {MODEL_DIR / 'model.pkl'}")


if __name__ == "__main__":
    main()
