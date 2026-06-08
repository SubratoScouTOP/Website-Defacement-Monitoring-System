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
    get_latest_hash
)
from detector import detect_change
from snapshot_manager import save_snapshot


def monitor_website():

    # Ensure database exists
    create_database()

    # Get previous hash from database
    previous_hash = get_latest_hash(TARGET_URL)

    # Fetch website HTML
    html_content = fetch_website()

    if not html_content:
        print("Failed to fetch website.")
        return

    # Parse DOM
    dom_content = extract_dom(html_content)

    # Generate current hash
    current_hash = generate_hash(dom_content)

    print("\n===================================")
    print("Current Hash:")
    print(current_hash)

    # Compare hashes
    result = detect_change(
        previous_hash,
        current_hash
    )

    print("\nDetection Result:")

    if result == "FIRST_RUN":
        print("First website snapshot recorded.")

    elif result == "NO_CHANGE":
        print("No changes detected.")

    elif result == "CHANGED":
        print("WARNING: Website content has changed!")

        # Save HTML snapshot when change detected
        save_snapshot(html_content)

    # Save latest hash to database
    save_hash(
        TARGET_URL,
        current_hash
    )

    print("===================================\n")


if __name__ == "__main__":

    # Run once immediately
    monitor_website()

    # Schedule periodic monitoring
    schedule.every(CHECK_INTERVAL).minutes.do(
        monitor_website
    )

    print("Monitoring started...")
    print(f"Checking every {CHECK_INTERVAL} minute(s).")
    print("Press CTRL + C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)