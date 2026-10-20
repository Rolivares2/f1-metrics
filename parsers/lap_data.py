import struct
from dataclasses import dataclass

from constants import PitStatus, DriverStatus, ResultStatus
from parser.header import HEADER_SIZE

_LAP = struct.Struct("<IIHBHBHBHBfff15BHHBfB")
LAP_SIZE = _LAP.size

@dataclass
class LapData:
    last_lap_time_ms: int
    current_lap_time_ms: int
    sector1_ms_part: int
    sector1_minutes_part: int
    sector2_ms_part: int
    sector2_minutes_part: int
    delta_to_car_in_front_ms_part: int
    delta_to_car_in_front_minutes_part: int
    delta_to_leader_ms_part: int
    delta_to_leader_minutes_part: int
    lap_distance: float
    total_distance: float
    safety_car_delta: float
    car_position: int
    current_lap_num: int
    pit_status: PitStatus
    num_pit_stops: int
    sector: int
    current_lap_invalid: bool
    penalties_s: int
    total_warnings: int
    corner_cutting_warnings: int
    unserved_drive_through_pens: int
    unserved_stop_go_pens: int
    grid_position: int
    driver_status: DriverStatus
    result_status: ResultStatus
    pit_lane_timer_active: bool
    pit_lane_time_ms: int
    pit_stop_timer_ms: int
    pit_stop_should_serve_pen: bool
    speed_trap_fastest_speed: float
    speed_trap_fastest_lap: int

    def __post_init__(self):
        self.pit_status = PitStatus(self.pit_status)
        self.driver_status = DriverStatus(self.driver_status)
        self.result_status = ResultStatus(self.result_status)
        self.current_lap_invalid = bool(self.current_lap_invalid)
        self.pit_lane_timer_active = bool(self.pit_lane_timer_active)
        self.pit_stop_should_serve_pen = bool(self.pit_stop_should_serve_pen)

    @property
    def sector1_time_ms(self) -> int:
        return self.sector1_minutes_part * 60_000 + self.sector1_ms_part

    @property
    def sector2_time_ms(self) -> int:
        return self.sector2_minutes_part * 60_000 + self.sector2_ms_part

    @property
    def delta_to_car_in_front_ms(self) -> int:
        return self.delta_to_car_in_front_minutes_part * 60_000 + self.delta_to_car_in_front_ms_part

    @property
    def delta_to_leader_ms(self) -> int:
        return self.delta_to_leader_minutes_part * 60_000 + self.delta_to_leader_ms_part

def parse_lap_data(data: bytes, car_index: int) -> LapData:
    v = _LAP.unpack_from(data, HEADER_SIZE + car_index * LAP_SIZE)
    return LapData(*v)