import sys
from pathlib import Path

# Add project root directory to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import requests
from config import TARGET_URL, TIMEOUT


def fetch_website():
    """
    Fetch HTML content from the target website.
    """

    try:
        response = requests.get(
            TARGET_URL,
            timeout=TIMEOUT
        )

        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as error:
        print(f"Error fetching website: {error}")
        return None


if __name__ == "__main__":

    html_content = fetch_website()

    if html_content:
        print("Website fetched successfully!\n")
        print(html_content[:500])