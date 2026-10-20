import struct
from dataclasses import dataclass

from constants import Team, Platform
from parsers.header import HEADER_SIZE

_CAR = struct.Struct("<7B32s2BHBB12B")
CAR_SIZE = _CAR.size
assert CAR_SIZE == 57


@dataclass
class Participant:
    ai_controlled: bool
    driver_id: int
    network_id: int
    team_id: int
    my_team: bool
    race_number: int
    nationality: int
    name: str
    telemetry_public: bool
    show_online_names: bool
    tech_level: int
    platform: Platform
    livery_colours: list

    @property
    def team(self):
        try:
            return Team(self.team_id)
        except ValueError:
            return None


def parse_participants(data: bytes) -> list:
    num_active = data[HEADER_SIZE]
    start = HEADER_SIZE + 1
    result = []

    for i in range(num_active):
        v = _CAR.unpack_from(data, start + i * CAR_SIZE)
        colours = v[13:25]
        result.append(Participant(
            ai_controlled=bool(v[0]),
            driver_id=v[1],
            network_id=v[2],
            team_id=v[3],
            my_team=bool(v[4]),
            race_number=v[5],
            nationality=v[6],
            name=v[7].split(b"\x00")[0].decode("utf-8", errors="replace"),
            telemetry_public=bool(v[8]),
            show_online_names=bool(v[9]),
            tech_level=v[10],
            platform=Platform(v[11]),
            livery_colours=[tuple(colours[j:j + 3]) for j in range(0, v[12] * 3, 3)],
        ))
    return result