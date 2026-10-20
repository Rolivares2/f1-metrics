import struct
from dataclasses import dataclass

_STRUCT = struct.Struct("<HBBBBBQfIIBB")
HEADER_SIZE = _STRUCT.size

@dataclass
class Header:
    packet_format: int
    game_year: int
    game_major: int
    game_minor: int
    packet_version: int
    packet_id: int
    session_uid: int
    session_time: float
    frame_id: int
    overall_frame_id: int
    secondary_player_car_idx: int
def parse_header(data: bytes) -> Header:
    return Header(*_STRUCT.unpack_from(data, 0))