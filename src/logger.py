from pathlib import Path
from datetime import datetime

LOG_FILE = (
    Path(__file__).resolve().parent.parent
    / "logs"
    / "monitor.log"
)


def write_log(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = f"{timestamp} - {message}\n"

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(log_entry)


if __name__ == "__main__":
    print("Logger module ready.")