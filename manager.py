from receiver import UDPReceiver
from parsers.header import parse_header
from parsers.car_telemetry import parse_car_telemetry

receiver = UDPReceiver()
for data in receiver.packets():
    header = parse_header(data)
    if header.packet_id == 6:
        car_telemetry = parse_car_telemetry(data, header.secondary_player_car_idx)
        print(f"{car_telemetry.speed} km/h | marcha {car_telemetry.speed} | rpm {car_telemetry.engine_rpm}")