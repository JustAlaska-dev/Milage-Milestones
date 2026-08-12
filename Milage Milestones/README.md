# ✈️ Mileage Milestones

A flight log that turns your total air miles into a year-long competition against real-world distance benchmarks — from a blue whale's annual migration loop up to the average distance from Earth to the Moon.

## How it works

- Log a flight by picking a departure and arrival airport and a date
- The backend calculates the real great-circle distance between those two airports using their actual coordinates (the haversine formula — the same math used for "as the crow flies" distance)
- Your total mileage across every logged flight is tracked against seven milestones, and the app shows exactly how far you are from the next one
- Everything is stored in a real SQLite database, so your flight history persists between sessions

## Milestones

| Level | Name | Benchmark | Target |
|---|---|---|---|
| 1 | The Ocean Cruiser | Blue Whale Annual Loop | 4,000 mi |
| 2 | The Sky Sovereign | Common Swift Endurance | 15,000 mi |
| 3 | The Explorer's Route | Great Equatorial Circumference | 25,000 mi |
| 4 | The Avian Overachiever | Arctic Tern Record | 60,000 mi |
| 5 | The Career Commuter | Standard Passenger Car Lifespan | 85,000 mi |
| 6 | The Final Frontier | Lunar Voyage | 238,855 mi |
| 7 | The Rock Star | Steve Aoki Tour Record | 241,850 mi |

## Tech stack

- **Backend**: Python (Flask) serving a small REST API
- **Database**: SQLite, with two tables — `airports` (a reference table of ~95 major airports with real coordinates) and `flights` (your logged flight history)
- **Frontend**: vanilla HTML, CSS, and JavaScript — no framework, calls the API with `fetch()`
- **Distance calculation**: the haversine formula, computed server-side in Python whenever a flight is logged, using miles as the unit throughout

## Running it locally

You'll need Python installed (see [python.org/downloads](https://www.python.org/downloads/) if you don't have it — on Windows, make sure to check "Add python.exe to PATH" during install).

1. Download or clone this repo
2. Open a terminal in the project folder
3. Install the one dependency:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database (only needs to be run once):
   ```bash
   python init_db.py
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open your browser to **http://127.0.0.1:5000**

Your flight data is saved locally in `flights.db` — it'll persist the next time you run the app.

## Adding more airports

The airport list in `airports_data.py` covers ~95 major hubs worldwide, but it isn't exhaustive. To add one, add a new row in the same format:

```python
("XXX", "Airport Name", "City", "Country", latitude, longitude)
```

Then re-run `python init_db.py` — it's safe to run again and won't erase your logged flights.

## Project structure

```
mileage-milestones/
├── app.py              # Flask backend + API routes + distance/milestone logic
├── init_db.py           # One-time database setup script
├── schema.sql            # SQL table definitions
├── airports_data.py      # Seed data: airport codes + coordinates
├── milestones_data.py     # Mileage milestone thresholds and facts
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```
