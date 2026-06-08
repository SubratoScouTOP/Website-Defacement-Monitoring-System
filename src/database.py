import sqlite3
from pathlib import Path
from datetime import datetime

DATABASE_PATH = Path(__file__).resolve().parent.parent / "data" / "hashes.db"


def create_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS website_hashes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        website TEXT NOT NULL,
        hash TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def save_hash(website, hash_value):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO website_hashes
    (timestamp, website, hash)
    VALUES (?, ?, ?)
    """, (timestamp, website, hash_value))

    connection.commit()
    connection.close()

    print("Hash saved successfully.")


def get_latest_hash(website):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT hash
    FROM website_hashes
    WHERE website = ?
    ORDER BY id DESC
    LIMIT 1
    """, (website,))

    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]

    return None


if __name__ == "__main__":
    create_database()
    print("Database ready.")