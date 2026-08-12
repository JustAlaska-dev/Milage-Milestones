"""
init_db.py

Run this once to create the SQLite database and seed it with airport data.
Safe to run again later — it won't duplicate airports or wipe existing
flights, since it uses INSERT OR IGNORE.

Usage:
    python init_db.py
"""

import sqlite3
from airports_data import AIRPORTS

DB_PATH = "flights.db"
SCHEMA_PATH = "schema.sql"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    cursor.executemany(
        """
        INSERT OR IGNORE INTO airports (code, name, city, country, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        AIRPORTS,
    )

    conn.commit()

    airport_count = cursor.execute("SELECT COUNT(*) FROM airports").fetchone()[0]
    flight_count = cursor.execute("SELECT COUNT(*) FROM flights").fetchone()[0]
    conn.close()

    print(f"Database ready at {DB_PATH}")
    print(f"  {airport_count} airports loaded")
    print(f"  {flight_count} flights currently logged")


if __name__ == "__main__":
    init_db()
