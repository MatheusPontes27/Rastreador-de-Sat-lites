from skyfield.api import Topos, load

# Carrega os dados TLE dos satélites
stations_url = 'https://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print(f"Loaded {len(satellites)} satellites")

# Seleciona o satélite desejado (ISS, neste caso)
satellite = {sat.name: sat for sat in satellites}['ISS (ZARYA)']

# Configura a localização do observador (latitude e longitude)
location = Topos(latitude_degrees=0.0, longitude_degrees=0.0)  # Ponto no Equador para simplificar

# Carrega o tempo atual
ts = load.timescale()
t = ts.now()

# Calcula a posição do satélite em relação à Terra
geocentric = satellite.at(t)

# Obtem latitude, longitude e altitude
subpoint = geocentric.subpoint()
print(f"Latitude: {subpoint.latitude.degrees:.2f}")
print(f"Longitude: {subpoint.longitude.degrees:.2f}")
print(f"Altitude: {subpoint.elevation.km:.2f} km")
