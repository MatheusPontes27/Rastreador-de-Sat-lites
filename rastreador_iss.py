from skyfield.api import Topos, load

stations_url = 'https://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print(f"Loaded {len(satellites)} satellites")

satellite = {sat.name: sat for sat in satellites}['ISS (ZARYA)']

location = Topos(latitude_degrees=0.0, longitude_degrees=0.0)  

ts = load.timescale()
t = ts.now()

geocentric = satellite.at(t)

subpoint = geocentric.subpoint()
print(f"Latitude: {subpoint.latitude.degrees:.2f}")
print(f"Longitude: {subpoint.longitude.degrees:.2f}")
print(f"Altitude: {subpoint.elevation.km:.2f} km")
