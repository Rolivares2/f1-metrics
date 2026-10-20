
import struct

from constants import PacketId
from parsers.header import parse_header
from parsers.lap_data import parse_lap_data
from parsers.car_setup import parse_car_setup
from parsers.car_telemetry import parse_car_telemetry
from parsers.car_status import parse_car_status
from parsers.participants import parse_participants
from parsers.final_classification import parse_final_classification

PACKET_FORMAT = 2025

PER_CAR_PARSERS = {
    PacketId.LAP_DATA: parse_lap_data,
    PacketId.CAR_SETUPS: parse_car_setup,
    PacketId.CAR_TELEMETRY: parse_car_telemetry,
    PacketId.CAR_STATUS: parse_car_status,
}

WHOLE_PACKET_PARSERS = {
    PacketId.PARTICIPANTS: parse_participants,
    PacketId.FINAL_CLASSIFICATION: parse_final_classification,
}

def parser_handler(data: bytes):
    try:
        header = parse_header(data)
    except struct.error:
        return None
    if header.packet_format != PACKET_FORMAT:
        return None

    try:
        packet_id = PacketId(header.packet_id)
    except ValueError:
        return None

    try:
        if packet_id in PER_CAR_PARSERS:
            result = PER_CAR_PARSERS[packet_id](data, header.player_car_index)
        elif packet_id in WHOLE_PACKET_PARSERS:
            result = WHOLE_PACKET_PARSERS[packet_id](data)
        else:
            return None
    except (struct.error, ValueError):
        return None
    return packet_id, result
