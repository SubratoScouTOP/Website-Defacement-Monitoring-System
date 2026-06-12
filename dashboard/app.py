import sqlite3
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_PATH = (
    PROJECT_ROOT
    / "data"
    / "hashes.db"
)

LOG_FILE = (
    PROJECT_ROOT
    / "logs"
    / "monitor.log"
)

SNAPSHOT_DIR = (
    PROJECT_ROOT
    / "snapshots"
)


def get_latest_record():

    try:

        connection = sqlite3.connect(
            DATABASE_PATH
        )

        cursor = connection.cursor()

        cursor.execute("""
        SELECT
            timestamp,
            website,
            hash
        FROM website_hashes
        ORDER BY id DESC
        LIMIT 1
        """)

        result = cursor.fetchone()

        connection.close()

        return result

    except Exception:

        return None


def get_recent_logs():

    if not LOG_FILE.exists():
        return []

    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        logs = file.readlines()

    return logs[-10:]


def get_snapshots():

    if not SNAPSHOT_DIR.exists():
        return []

    snapshots = []

    for file in SNAPSHOT_DIR.iterdir():

        if file.is_file():

            snapshots.append(
                file.name
            )

    snapshots.sort(reverse=True)

    return snapshots


@app.route("/")
def dashboard():

    latest = get_latest_record()

    logs = get_recent_logs()

    snapshots = get_snapshots()

    return render_template(
        "index.html",
        latest=latest,
        logs=logs,
        snapshots=snapshots
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )