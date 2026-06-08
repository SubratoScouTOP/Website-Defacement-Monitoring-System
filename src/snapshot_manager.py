from pathlib import Path
from datetime import datetime

SNAPSHOT_DIR = (
    Path(__file__).resolve().parent.parent
    / "snapshots"
)


def save_snapshot(html_content):

    SNAPSHOT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        SNAPSHOT_DIR
        / f"snapshot_{timestamp}.html"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html_content)

    print(f"Snapshot saved: {filename.name}")