import krpc

conn = krpc.connect(name='Hello World')

vessel = conn.space_center.active_vessel

print(vessel.name)
vessel.name = "My Vessel"

flight_info = vessel.flight()

print(vessel.name)
print(flight_info.mean_altitude)