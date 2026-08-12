"""
app.py

Flask backend for the Mileage Milestones tracker.

WHAT THIS SERVES
-----------------
- The frontend page (templates/index.html)
- A small REST API the frontend's JavaScript talks to:
    GET    /api/airports        -> list of all known airports (for the dropdowns)
    GET    /api/flights         -> every flight logged so far, most recent first
    POST   /api/flights         -> log a new flight (calculates distance server-side)
    DELETE /api/flights/<id>    -> remove a logged flight
    GET    /api/milestones      -> total miles flown + current/next milestone

HOW DISTANCE IS CALCULATED
----------------------------
Distance between two airports is computed with the haversine formula —
a standard way to calculate the great-circle distance between two points
on a sphere given their latitude/longitude. This is the straight-line
distance "as the crow flies," not the exact path a plane's route takes,
so real flown distance is usually a bit longer. Good enough for tracking
progress toward a mileage milestone.
"""

import math
import sqlite3
from datetime import datetime

from flask import Flask, jsonify, request, render_template, g

from milestones_data import MILESTONES

app = Flask(__name__)
DB_PATH = "flights.db"


def get_db():
    """Get (or create) the database connection for this request."""
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def haversine_miles(lat1, lon1, lat2, lon2):
    """
    Great-circle distance between two lat/lon points, in miles.
    Standard haversine formula, using Earth's mean radius in miles.
    """
    R = 3958.8  # Earth's mean radius in miles

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)

    a = (
        math.sin(d_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def get_milestone_progress(total_miles):
    """
    Given a total distance flown, figure out which milestone has most
    recently been passed and how far along progress is to the next one.
    """
    current = None
    nxt = None

    for m in MILESTONES:
        if total_miles >= m["miles"]:
            current = m
        else:
            nxt = m
            break

    if current is None:
        nxt = MILESTONES[0]
        progress_pct = (total_miles / nxt["miles"]) * 100
        return {
            "total_miles": round(total_miles, 1),
            "current_milestone": None,
            "next_milestone": nxt,
            "progress_pct": round(min(progress_pct, 100), 1),
            "miles_to_next": round(nxt["miles"] - total_miles, 1),
        }

    if nxt is None:
        return {
            "total_miles": round(total_miles, 1),
            "current_milestone": current,
            "next_milestone": None,
            "progress_pct": 100.0,
            "miles_to_next": 0,
        }

    span = nxt["miles"] - current["miles"]
    progress_into_span = total_miles - current["miles"]
    progress_pct = (progress_into_span / span) * 100

    return {
        "total_miles": round(total_miles, 1),
        "current_milestone": current,
        "next_milestone": nxt,
        "progress_pct": round(progress_pct, 1),
        "miles_to_next": round(nxt["miles"] - total_miles, 1),
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/airports")
def api_airports():
    db = get_db()
    rows = db.execute(
        "SELECT code, name, city, country FROM airports ORDER BY city"
    ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/flights")
def api_flights():
    db = get_db()
    rows = db.execute(
        """
        SELECT f.id, f.flight_date, f.departure_code, f.arrival_code,
               f.distance_miles, f.notes,
               dep.city AS departure_city, arr.city AS arrival_city
        FROM flights f
        JOIN airports dep ON f.departure_code = dep.code
        JOIN airports arr ON f.arrival_code = arr.code
        ORDER BY f.flight_date DESC, f.id DESC
        """
    ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/flights", methods=["POST"])
def add_flight():
    data = request.get_json(force=True)

    flight_date = data.get("flight_date", "").strip()
    departure_code = data.get("departure_code", "").strip().upper()
    arrival_code = data.get("arrival_code", "").strip().upper()
    notes = data.get("notes", "").strip()

    if not flight_date or not departure_code or not arrival_code:
        return jsonify({"error": "flight_date, departure_code, and arrival_code are required"}), 400

    if departure_code == arrival_code:
        return jsonify({"error": "Departure and arrival airports can't be the same"}), 400

    db = get_db()
    dep = db.execute("SELECT * FROM airports WHERE code = ?", (departure_code,)).fetchone()
    arr = db.execute("SELECT * FROM airports WHERE code = ?", (arrival_code,)).fetchone()

    if dep is None:
        return jsonify({"error": f"Unknown departure airport code: {departure_code}"}), 400
    if arr is None:
        return jsonify({"error": f"Unknown arrival airport code: {arrival_code}"}), 400

    try:
        datetime.strptime(flight_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "flight_date must be in YYYY-MM-DD format"}), 400

    distance = haversine_miles(dep["latitude"], dep["longitude"], arr["latitude"], arr["longitude"])

    cursor = db.execute(
        """
        INSERT INTO flights (flight_date, departure_code, arrival_code, distance_miles, notes)
        VALUES (?, ?, ?, ?, ?)
        """,
        (flight_date, departure_code, arrival_code, distance, notes),
    )
    db.commit()

    return jsonify({
        "id": cursor.lastrowid,
        "flight_date": flight_date,
        "departure_code": departure_code,
        "arrival_code": arrival_code,
        "distance_miles": round(distance, 1),
        "notes": notes,
    }), 201


@app.route("/api/flights/<int:flight_id>", methods=["DELETE"])
def delete_flight(flight_id):
    db = get_db()
    result = db.execute("DELETE FROM flights WHERE id = ?", (flight_id,))
    db.commit()

    if result.rowcount == 0:
        return jsonify({"error": "Flight not found"}), 404

    return jsonify({"deleted": flight_id})


@app.route("/api/milestones")
def api_milestones():
    db = get_db()
    total = db.execute("SELECT COALESCE(SUM(distance_miles), 0) AS total FROM flights").fetchone()["total"]
    progress = get_milestone_progress(total)
    progress["all_milestones"] = MILESTONES
    return jsonify(progress)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
