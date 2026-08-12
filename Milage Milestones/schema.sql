-- schema.sql
-- Defines the two tables this app runs on.
--
-- airports: a reference table of airport codes and their coordinates,
--           used to calculate distance between any two airports.
-- flights:  the actual flight log a user builds up over time.

CREATE TABLE IF NOT EXISTS airports (
    code TEXT PRIMARY KEY,       -- IATA code, e.g. 'JFK'
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_date TEXT NOT NULL,          -- ISO date string, e.g. '2026-03-14'
    departure_code TEXT NOT NULL,
    arrival_code TEXT NOT NULL,
    distance_miles REAL NOT NULL,       -- calculated once at insert time
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (departure_code) REFERENCES airports(code),
    FOREIGN KEY (arrival_code) REFERENCES airports(code)
);

CREATE INDEX IF NOT EXISTS idx_flights_date ON flights(flight_date);
