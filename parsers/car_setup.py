import struct
from dataclasses import dataclass
from parsers.header import HEADER_SIZE

_SETUP = struct.Struct("<BBBBffffBBBBBBBBBffffBf")
SETUP_SIZE = _SETUP.size

@dataclass
class CarSetup:
    front_wing: int
    rear_wing: int
    on_throttle: int
    off_throttle: int
    front_camber: float
    rear_camber: float
    front_toe: float
    rear_toe: float
    front_suspension: int
    rear_suspension: int
    front_anti_roll: int
    rear_anti_roll: int
    front_suspension_height: int
    rear_suspension_height: int
    brake_pressure: int
    brake_bias: int
    engine_braking: int
    rl_tyre_pressure: float
    rr_tyre_pressure: float
    fl_tyre_pressure: float
    fr_tyre_pressure: float
    ballast: int
    fuel_load: float

def parse_car_setup(data: bytes, car_index: int) -> CarSetup:
    v = _SETUP.unpack_from(data, HEADER_SIZE + car_index * SETUP_SIZE)
    return CarSetup(*v)