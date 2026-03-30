import time

from backend.anamoly.detection import detect_anomaly
from backend.config.dask_config import start_dask
from backend.config.email_alert_config import send_anomaly_email
from backend.pipeline.processing import build_pipeline

ADMIN_EMAIL = "rakshakcarvlho2311@gmail.com"


def main():
    client = start_dask()
    try:
        print(client)
        print(f"Dashboard link: {client.dashboard_link}")
        print("\n" + "=" * 50)

        start = time.time()
        log_df = build_pipeline(r"backend/sample_data/log_data.log")
        total_logs = log_df.shape[0].compute()
        end = time.time()

        print("Total logs parsed:", total_logs)
        print("Time taken:", round(end - start, 2), "seconds")
        print("\nRunning anomaly detection...")

        anomalies = detect_anomaly(log_df)
        if anomalies.empty:
            print("No anomalies detected")
        else:
            print(f"{len(anomalies)} anomalies detected!")

            for _, row in anomalies.iterrows():
                anomaly_data = {
                    "timestamp": row["timestamp"],
                    "error_count": row["error_count"],
                    "z_score": row["z_score"],
                }

                try:
                    send_anomaly_email(to_email=ADMIN_EMAIL, anomaly=anomaly_data)
                    print(
                        f"Alert sent | Time: {row['timestamp']} | "
                        f"Errors: {row['error_count']}"
                    )
                except RuntimeError as exc:
                    print(f"Email skipped: {exc}")
                    break
    finally:
        client.close()

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
