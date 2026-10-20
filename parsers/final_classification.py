import struct
from dataclasses import dataclass

from constants import (ResultStatus, ResultReason,
                       ActualTyreCompound, VisualTyreCompound)
from parsers.header import HEADER_SIZE

_CAR = struct.Struct("<BBBBBBBIdBBB8B8B8B")
CAR_SIZE = _CAR.size
assert CAR_SIZE == 46


@dataclass
class FinalClassification:
    position: int
    num_laps: int
    grid_position: int
    points: int
    num_pit_stops: int
    result_status: ResultStatus
    result_reason: ResultReason
    best_lap_time_ms: int
    total_race_time_s: float
    penalties_time_s: int
    num_penalties: int
    tyre_stints_actual: list
    tyre_stints_visual: list
    tyre_stints_end_laps: list


def parse_final_classification(data: bytes) -> list:
    num_cars = data[HEADER_SIZE]
    start = HEADER_SIZE + 1
    results = []

    for i in range(num_cars):
        v = _CAR.unpack_from(data, start + i * CAR_SIZE)
        n_stints = v[11]
        results.append(FinalClassification(
            position=v[0],
            num_laps=v[1],
            grid_position=v[2],
            points=v[3],
            num_pit_stops=v[4],
            result_status=ResultStatus(v[5]),
            result_reason=ResultReason(v[6]),
            best_lap_time_ms=v[7],
            total_race_time_s=v[8],
            penalties_time_s=v[9],
            num_penalties=v[10],
            tyre_stints_actual=[ActualTyreCompound(c) for c in v[12:20][:n_stints]],
            tyre_stints_visual=[VisualTyreCompound(c) for c in v[20:28][:n_stints]],
            tyre_stints_end_laps=list(v[28:36][:n_stints]),
        ))
    return results