import sys
from pathlib import Path
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Add project root directory
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from config import (
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER,
    SMTP_SERVER,
    SMTP_PORT
)


def send_alert(
    website,
    severity,
    similarity
):

    try:

        subject = (
            "[ALERT] Website Change Detected"
        )

        body = f"""
Website Defacement Alert

Website:
{website}

Severity:
{severity}

Similarity:
{similarity:.2f}%

Please investigate immediately.
"""

        message = MIMEMultipart()

        message["From"] = EMAIL_SENDER
        message["To"] = EMAIL_RECEIVER
        message["Subject"] = subject

        message.attach(
            MIMEText(
                body,
                "plain"
            )
        )

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        )

        server.starttls()

        server.login(
            EMAIL_SENDER,
            EMAIL_PASSWORD
        )

        server.sendmail(
            EMAIL_SENDER,
            EMAIL_RECEIVER,
            message.as_string()
        )

        server.quit()

        print(
            "Alert email sent successfully."
        )

        return True

    except Exception as error:

        print(
            f"Email error: {error}"
        )

        return False


if __name__ == "__main__":

    send_alert(
        "https://example.com",
        "HIGH",
        45.50
    )