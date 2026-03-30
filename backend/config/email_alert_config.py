import os
import smtplib
from email.message import EmailMessage
from typing import Dict

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL = "rakshak103@gmail.com"
PASSWORD = "fhjq ilbe cnia ygtp"


def send_anomaly_email(to_email: str, anomaly: Dict):
    if not EMAIL or not PASSWORD:
        raise RuntimeError(
            "Missing email credentials. Set ALERT_EMAIL and ALERT_EMAIL_PASSWORD."
        )

    subject = "Log Anomaly Detected"
    body = f"""
Anomaly Detected in System Logs

Time Window : {anomaly['timestamp']}
Error Count : {anomaly['error_count']}
Z-Score     : {round(float(anomaly['z_score']), 2)}

Please investigate immediately.

Regards,
Log Monitoring System
"""

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
