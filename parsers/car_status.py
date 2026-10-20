import struct
from dataclasses import dataclass
from constants import (
    TractionControl, FuelMix, ActualTyreCompound, 
    VisualTyreCompound, FiaFlag, ErsDeployMode
    )
from parsers.header import HEADER_SIZE

_STATUS = struct.Struct("<BBBBBfffHHBBHBBBbfffBfffB")
STATUS_SIZE = _STATUS.size

@dataclass
class CarStatus:
    traction_control: TractionControl
    abs: int
    fuel_mix: int
    front_brake_bias: int
    pit_limiter_status: int
    fuel_in_tank: float
    fuel_capacity: float
    fuel_remaining_laps: float
    max_rpm: int
    idle_rpm: int
    max_gear: int
    drs_allowed: int
    drs_activation_distance: int
    actual_tyre_compound: ActualTyreCompound
    visual_tyre_compound: VisualTyreCompound
    tyre_age_laps: int
    vehicle_fia_flags: FiaFlag
    engine_power_ice: float
    engine_power_mguk: float
    ers_store_energy: float
    ers_deploy_mode: ErsDeployMode
    ers_harvested_mguk: float
    ers_harvested_mguh: float
    ers_deployed: float
    network_paused: int
    def __post_init__(self):
        # Convierte los códigos numéricos en enums justo después de crear el objeto
        self.traction_control = TractionControl(self.traction_control)
        self.fuel_mix = FuelMix(self.fuel_mix)
        self.actual_tyre_compound = ActualTyreCompound(self.actual_tyre_compound)
        self.visual_tyre_compound = VisualTyreCompound(self.visual_tyre_compound)
        self.vehicle_fia_flags = FiaFlag(self.vehicle_fia_flags)
        self.ers_deploy_mode = ErsDeployMode(self.ers_deploy_mode)

def parse_car_status(data: bytes, car_index: int) -> CarStatus:
    v = _STATUS.unpack_from(data, HEADER_SIZE + car_index * STATUS_SIZE)
    return CarStatus(*v)