import sys
from pathlib import Path
import time
import schedule

# Add project root directory
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from config import TARGET_URL, CHECK_INTERVAL

from fetcher import fetch_website
from parser import extract_dom
from hasher import generate_hash

from database import (
    create_database,
    save_hash,
    get_latest_hash,
    get_latest_dom
)

from detector import detect_change
from snapshot_manager import save_snapshot
from logger import write_log

from similarity import calculate_similarity
from severity import get_severity


def monitor_website():

    create_database()

    previous_hash = get_latest_hash(
        TARGET_URL
    )

    previous_dom = get_latest_dom(
        TARGET_URL
    )

    html_content = fetch_website()

    if not html_content:

        message = "Failed to fetch website."

        print(message)
        write_log(message)

        return

    dom_content = extract_dom(
        html_content
    )

    current_hash = generate_hash(
        dom_content
    )

    print("\n===================================")
    print("Current Hash:")
    print(current_hash)

    result = detect_change(
        previous_hash,
        current_hash
    )

    print("\nDetection Result:")

    if result == "FIRST_RUN":

        message = (
            "First website snapshot recorded."
        )

        print(message)
        write_log(message)

    elif result == "NO_CHANGE":

        message = (
            "No changes detected."
        )

        print(message)
        write_log(message)

    elif result == "CHANGED":

        print(
            "Website content changed."
        )

        write_log(
            "Website content changed."
        )

        if previous_dom:

            similarity_score = calculate_similarity(
                previous_dom,
                dom_content
            )

            severity = get_severity(
                similarity_score
            )

            print(
                f"Similarity: {similarity_score}%"
            )

            print(
                f"Severity: {severity}"
            )

            write_log(
                f"Similarity: {similarity_score}%"
            )

            write_log(
                f"Severity: {severity}"
            )

            if severity in [
                "HIGH",
                "CRITICAL"
            ]:

                save_snapshot(
                    html_content
                )

                write_log(
                    "Snapshot saved."
                )

    save_hash(
        TARGET_URL,
        current_hash,
        dom_content
    )

    write_log(
        f"Hash saved for {TARGET_URL}"
    )

    print("===================================\n")


if __name__ == "__main__":

    monitor_website()

    schedule.every(
        CHECK_INTERVAL
    ).minutes.do(
        monitor_website
    )

    print("Monitoring started...")
    print(
        f"Checking every {CHECK_INTERVAL} minute(s)."
    )
    print(
        "Press CTRL + C to stop.\n"
    )

    while True:

        schedule.run_pending()
        time.sleep(1)