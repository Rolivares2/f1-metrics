# constants.py
from enum import Enum


class PacketId(Enum):
    MOTION = 0
    SESSION = 1
    LAP_DATA = 2
    EVENT = 3
    PARTICIPANTS = 4
    CAR_SETUPS = 5
    CAR_TELEMETRY = 6
    CAR_STATUS = 7
    FINAL_CLASSIFICATION = 8
    LOBBY_INFO = 9
    CAR_DAMAGE = 10
    SESSION_HISTORY = 11
    TYRE_SETS = 12
    MOTION_EX = 13
    TIME_TRIAL = 14
    LAP_POSITIONS = 15


class SurfaceType(Enum):
    TARMAC = 0
    RUMBLE_STRIP = 1
    CONCRETE = 2
    ROCK = 3
    GRAVEL = 4
    MUD = 5
    SAND = 6
    GRASS = 7
    WATER = 8
    COBBLESTONE = 9
    METAL = 10
    RIDGED = 11


class TractionControl(Enum):
    OFF = 0
    MEDIUM = 1
    FULL = 2


class FuelMix(Enum):
    LEAN = 0
    STANDARD = 1
    RICH = 2
    MAX = 3


class ActualTyreCompound(Enum):
    C5 = 16
    C4 = 17
    C3 = 18
    C2 = 19
    C1 = 20
    C0 = 21
    C6 = 22
    INTER = 7
    WET = 8


class VisualTyreCompound(Enum):
    SOFT = 16
    MEDIUM = 17
    HARD = 18
    INTER = 7
    WET = 8


class FiaFlag(Enum):
    UNKNOWN = -1
    NONE = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3


class ErsDeployMode(Enum):
    NONE = 0
    MEDIUM = 1
    HOTLAP = 2
    OVERTAKE = 3