"""
milestones_data.py

Mileage milestones used as level thresholds, ordered smallest to largest.
Each one pairs a real-world distance benchmark with a target mile count
for the tracker.

Note: Level 6 and 7 targets from the original brief (Rock Star Tour Record
at 241,850 mi and Lunar Voyage at 238,855 mi) were supplied out of order —
since 238,855 < 241,850, they're arranged here by actual distance so the
tracker's progress bar always moves forward correctly.
"""

MILESTONES = [
    {
        "name": "The Ocean Cruiser",
        "subtitle": "The Blue Whale Annual Loop",
        "miles": 4000,
        "fact": "You've out-traveled the standard annual feeding and breeding migration loop of the largest animal to ever exist on Earth.",
    },
    {
        "name": "The Sky Sovereign",
        "subtitle": "The Common Swift Endurance",
        "miles": 15000,
        "fact": "You've beaten the annual migration distance of the Common Swift — a bird that spends nearly 10 consecutive months entirely in the air without landing.",
    },
    {
        "name": "The Explorer's Route",
        "subtitle": "The Great Equatorial Circumference",
        "miles": 25000,
        "fact": "You've flown the exact linear distance required to wrap a measuring tape all the way around the Earth's equator.",
    },
    {
        "name": "The Avian Overachiever",
        "subtitle": "The Arctic Tern Record",
        "miles": 60000,
        "fact": "You've officially surpassed the highest individually tracked animal migration ever recorded by scientists — a winding pole-to-pole loop by a single super-migrant Arctic Tern.",
    },
    {
        "name": "The Career Commuter",
        "subtitle": "The Standard Passenger Car Lifespan",
        "miles": 85000,
        "fact": "You've compressed what an average person drives in an entire decade of commuting into a single calendar year of work.",
    },
    {
        "name": "The Final Frontier",
        "subtitle": "The Lunar Voyage",
        "miles": 238855,
        "fact": "You've flown the exact average distance from the surface of the Earth to the Moon.",
    },
    {
        "name": "The Rock Star",
        "subtitle": "The Steve Aoki Tour Record",
        "miles": 241850,
        "fact": "You've flown further in a year than DJ Steve Aoki did during his peak touring schedule — a record for the most traveled musician in a single year. The ultimate tracker reward.",
    },
]

