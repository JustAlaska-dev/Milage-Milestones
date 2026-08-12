"""
airports_data.py

A curated reference list of major airports and their real coordinates.
Used to calculate great-circle distance between any two airports a flight
was logged between. This is not exhaustive — it covers major hubs across
North America, Latin America, Europe, the Middle East, Africa, Asia, and
Oceania. If an airport you need isn't here, add a row to this list in the
same format: (IATA code, name, city, country, latitude, longitude).
"""

AIRPORTS = [
    # --- United States ---
    ("JFK", "John F. Kennedy International", "New York", "USA", 40.6413, -73.7781),
    ("LGA", "LaGuardia", "New York", "USA", 40.7769, -73.8740),
    ("EWR", "Newark Liberty International", "Newark", "USA", 40.6895, -74.1745),
    ("LAX", "Los Angeles International", "Los Angeles", "USA", 33.9416, -118.4085),
    ("SFO", "San Francisco International", "San Francisco", "USA", 37.6213, -122.3790),
    ("ORD", "O'Hare International", "Chicago", "USA", 41.9742, -87.9073),
    ("ATL", "Hartsfield-Jackson", "Atlanta", "USA", 33.6407, -84.4277),
    ("DFW", "Dallas/Fort Worth International", "Dallas", "USA", 32.8998, -97.0403),
    ("DEN", "Denver International", "Denver", "USA", 39.8561, -104.6737),
    ("SEA", "Seattle-Tacoma International", "Seattle", "USA", 47.4502, -122.3088),
    ("MIA", "Miami International", "Miami", "USA", 25.7959, -80.2870),
    ("LAS", "Harry Reid International", "Las Vegas", "USA", 36.0840, -115.1537),
    ("PHX", "Phoenix Sky Harbor", "Phoenix", "USA", 33.4373, -112.0078),
    ("IAH", "George Bush Intercontinental", "Houston", "USA", 29.9902, -95.3368),
    ("MCO", "Orlando International", "Orlando", "USA", 28.4312, -81.3081),
    ("MSP", "Minneapolis-St Paul International", "Minneapolis", "USA", 44.8848, -93.2223),
    ("DTW", "Detroit Metro", "Detroit", "USA", 42.2124, -83.3534),
    ("PHL", "Philadelphia International", "Philadelphia", "USA", 39.8744, -75.2424),
    ("BOS", "Logan International", "Boston", "USA", 42.3656, -71.0096),
    ("FLL", "Fort Lauderdale-Hollywood", "Fort Lauderdale", "USA", 26.0726, -80.1527),
    ("BWI", "Baltimore/Washington International", "Baltimore", "USA", 39.1774, -76.6684),
    ("SLC", "Salt Lake City International", "Salt Lake City", "USA", 40.7884, -111.9778),
    ("SAN", "San Diego International", "San Diego", "USA", 32.7338, -117.1933),
    ("TPA", "Tampa International", "Tampa", "USA", 27.9755, -82.5332),
    ("PDX", "Portland International", "Portland", "USA", 45.5898, -122.5951),
    ("STL", "St Louis Lambert International", "St Louis", "USA", 38.7487, -90.3700),
    ("CLT", "Charlotte Douglas International", "Charlotte", "USA", 35.2140, -80.9431),
    ("DCA", "Reagan National", "Washington D.C.", "USA", 38.8512, -77.0402),
    ("IAD", "Washington Dulles International", "Washington D.C.", "USA", 38.9531, -77.4565),
    ("AUS", "Austin-Bergstrom International", "Austin", "USA", 30.1975, -97.6664),
    ("RDU", "Raleigh-Durham International", "Raleigh", "USA", 35.8776, -78.7875),
    ("BNA", "Nashville International", "Nashville", "USA", 36.1263, -86.6774),
    ("MCI", "Kansas City International", "Kansas City", "USA", 39.2976, -94.7139),
    ("MEM", "Memphis International", "Memphis", "USA", 35.0424, -89.9767),
    ("CVG", "Cincinnati/N Kentucky International", "Cincinnati", "USA", 39.0489, -84.6678),
    ("IND", "Indianapolis International", "Indianapolis", "USA", 39.7173, -86.2944),
    ("CLE", "Cleveland Hopkins International", "Cleveland", "USA", 41.4117, -81.8498),
    ("PIT", "Pittsburgh International", "Pittsburgh", "USA", 40.4915, -80.2329),

    # --- Canada ---
    ("YYZ", "Toronto Pearson International", "Toronto", "Canada", 43.6777, -79.6248),
    ("YVR", "Vancouver International", "Vancouver", "Canada", 49.1967, -123.1815),
    ("YUL", "Montreal-Trudeau International", "Montreal", "Canada", 45.4706, -73.7408),

    # --- Latin America ---
    ("MEX", "Mexico City International", "Mexico City", "Mexico", 19.4363, -99.0721),
    ("GRU", "Sao Paulo/Guarulhos International", "Sao Paulo", "Brazil", -23.4356, -46.4731),
    ("EZE", "Ministro Pistarini International", "Buenos Aires", "Argentina", -34.8222, -58.5358),
    ("SCL", "Arturo Merino Benitez International", "Santiago", "Chile", -33.3930, -70.7858),
    ("BOG", "El Dorado International", "Bogota", "Colombia", 4.7016, -74.1469),
    ("LIM", "Jorge Chavez International", "Lima", "Peru", -12.0219, -77.1143),
    ("PTY", "Tocumen International", "Panama City", "Panama", 9.0714, -79.3835),

    # --- Europe ---
    ("LHR", "Heathrow", "London", "UK", 51.4700, -0.4543),
    ("LGW", "Gatwick", "London", "UK", 51.1537, -0.1821),
    ("CDG", "Charles de Gaulle", "Paris", "France", 49.0097, 2.5479),
    ("FRA", "Frankfurt Airport", "Frankfurt", "Germany", 50.0379, 8.5622),
    ("MUC", "Munich Airport", "Munich", "Germany", 48.3538, 11.7861),
    ("AMS", "Schiphol", "Amsterdam", "Netherlands", 52.3105, 4.7683),
    ("MAD", "Adolfo Suarez Madrid-Barajas", "Madrid", "Spain", 40.4983, -3.5676),
    ("BCN", "Barcelona-El Prat", "Barcelona", "Spain", 41.2974, 2.0833),
    ("FCO", "Leonardo da Vinci-Fiumicino", "Rome", "Italy", 41.8003, 12.2389),
    ("ZRH", "Zurich Airport", "Zurich", "Switzerland", 47.4647, 8.5492),
    ("VIE", "Vienna International", "Vienna", "Austria", 48.1103, 16.5697),
    ("CPH", "Copenhagen Airport", "Copenhagen", "Denmark", 55.6180, 12.6560),
    ("ARN", "Stockholm Arlanda", "Stockholm", "Sweden", 59.6519, 17.9186),
    ("OSL", "Oslo Airport", "Oslo", "Norway", 60.1976, 11.1004),
    ("HEL", "Helsinki-Vantaa", "Helsinki", "Finland", 60.3172, 24.9633),
    ("DUB", "Dublin Airport", "Dublin", "Ireland", 53.4213, -6.2701),
    ("LIS", "Humberto Delgado Airport", "Lisbon", "Portugal", 38.7813, -9.1359),
    ("ATH", "Athens International", "Athens", "Greece", 37.9364, 23.9445),
    ("IST", "Istanbul Airport", "Istanbul", "Turkey", 41.2753, 28.7519),
    ("WAW", "Warsaw Chopin", "Warsaw", "Poland", 52.1657, 20.9671),
    ("PRG", "Vaclav Havel Airport", "Prague", "Czechia", 50.1008, 14.2600),
    ("BRU", "Brussels Airport", "Brussels", "Belgium", 50.9014, 4.4844),

    # --- Middle East / Africa ---
    ("DXB", "Dubai International", "Dubai", "UAE", 25.2532, 55.3657),
    ("DOH", "Hamad International", "Doha", "Qatar", 25.2731, 51.6081),
    ("AUH", "Zayed International", "Abu Dhabi", "UAE", 24.4330, 54.6511),
    ("CAI", "Cairo International", "Cairo", "Egypt", 30.1219, 31.4056),
    ("JNB", "O.R. Tambo International", "Johannesburg", "South Africa", -26.1392, 28.2460),
    ("NBO", "Jomo Kenyatta International", "Nairobi", "Kenya", -1.3192, 36.9278),
    ("LOS", "Murtala Muhammed International", "Lagos", "Nigeria", 6.5774, 3.3212),

    # --- Asia ---
    ("SIN", "Changi Airport", "Singapore", "Singapore", 1.3644, 103.9915),
    ("HKG", "Hong Kong International", "Hong Kong", "Hong Kong", 22.3080, 113.9185),
    ("NRT", "Narita International", "Tokyo", "Japan", 35.7720, 140.3929),
    ("HND", "Haneda Airport", "Tokyo", "Japan", 35.5494, 139.7798),
    ("ICN", "Incheon International", "Seoul", "South Korea", 37.4602, 126.4407),
    ("PEK", "Beijing Capital International", "Beijing", "China", 40.0799, 116.6031),
    ("PVG", "Shanghai Pudong International", "Shanghai", "China", 31.1443, 121.8083),
    ("BKK", "Suvarnabhumi Airport", "Bangkok", "Thailand", 13.6900, 100.7501),
    ("KUL", "Kuala Lumpur International", "Kuala Lumpur", "Malaysia", 2.7456, 101.7099),
    ("DEL", "Indira Gandhi International", "Delhi", "India", 28.5562, 77.1000),
    ("BOM", "Chhatrapati Shivaji International", "Mumbai", "India", 19.0896, 72.8656),
    ("MNL", "Ninoy Aquino International", "Manila", "Philippines", 14.5086, 121.0198),
    ("CGK", "Soekarno-Hatta International", "Jakarta", "Indonesia", -6.1256, 106.6559),
    ("TPE", "Taiwan Taoyuan International", "Taipei", "Taiwan", 25.0797, 121.2342),

    # --- Oceania ---
    ("SYD", "Sydney Kingsford Smith", "Sydney", "Australia", -33.9399, 151.1753),
    ("MEL", "Melbourne Airport", "Melbourne", "Australia", -37.6690, 144.8410),
    ("AKL", "Auckland Airport", "Auckland", "New Zealand", -37.0082, 174.7850),
    ("BNE", "Brisbane Airport", "Brisbane", "Australia", -27.3842, 153.1175),
    ("PER", "Perth Airport", "Perth", "Australia", -31.9403, 115.9669),
]
