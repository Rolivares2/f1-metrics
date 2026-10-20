import struct
from dataclasses import dataclass
from parsers.header import HEADER_SIZE

_CAR = struct.Struct("<HfffBbHBBH4H4B4BH4f4B")
CAR_SIZE = _CAR.size

@dataclass
class CarTelemetry:
    speed: int
    throttle: float
    steer: float
    brake: float
    clutch: int
    gear: int
    engine_rpm: int
    drs: int
    rev_lights_percent: int
    rev_lights_bits: int
    brakes_temp: tuple
    tyres_surface_temp: tuple
    tyres_inner_temp: tuple
    engine_temp: int
    tyres_pressure: tuple
    surface_type: tuple

def parse_car_telemetry(data: bytes, car_index: int) -> CarTelemetry:
    v = _CAR.unpack_from(data, HEADER_SIZE + car_index * CAR_SIZE)
    return CarTelemetry(speed=v[0], throttle=v[1], steer=v[2], brake=v[3], clutch=v[4], gear=v[5], 
                        rpm=v[6], drs=v[7], rev_lights_percent=v[8], rev_lights_bits=v[9],
                        brakes_temp=v[10:14], tyres_surface_temp=v[14:18], engine_temp=v[22],
                        tyres_pressure=v[23:27], surface_type=v[27:31])