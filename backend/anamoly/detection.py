# Here we detect anomalies from log data by comparing current errors
# with typical error volume using a simple z-score.

import dask.dataframe as dd
import pandas as pd


def detect_anamoly(log_df, z_threshold=3):
    if "timestamp" not in log_df.columns or "level" not in log_df.columns:
        raise ValueError("log_df must contain 'timestamp' and 'level' columns")

    prepared_df = log_df.assign(timestamp=dd.to_datetime(log_df["timestamp"]))
    error_logs = prepared_df[prepared_df["level"] == "ERROR"].assign(
        minute=lambda df: df["timestamp"].dt.floor("min")
    )

    error_counts = (
        error_logs.groupby("minute")
        .size()
        .rename("error_count")
        .reset_index()
    )

    counts_df = error_counts.compute()
    if counts_df.empty:
        return pd.DataFrame(columns=["timestamp", "error_count", "z_score"])

    counts_df = counts_df.rename(columns={"minute": "timestamp"})
    mean = counts_df["error_count"].mean()
    std = counts_df["error_count"].std()

    if not std or pd.isna(std):
        return pd.DataFrame(columns=["timestamp", "error_count", "z_score"])

    counts_df["z_score"] = (counts_df["error_count"] - mean) / std
    return counts_df[counts_df["z_score"].abs() > z_threshold][
        ["timestamp", "error_count", "z_score"]
    ].reset_index(drop=True)


def detect_anomaly(log_df, z_threshold=3):
    """Correctly spelled wrapper for callers."""
    return detect_anamoly(log_df, z_threshold=z_threshold)
