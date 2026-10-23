# f1-metrics
A free and open-source app to visualize real-time telemetry from F1 25, decoded from the game's UDP output.
## How it works
F1 25 broadcast telemetry over UDP. Each packet is a packed, little-endian C struct. This project receives those packets, decodes them with Python's `struct` module, and turns them into readable Python objects. A React web app is meant to visualize that data.
```
F1 25 --UDP--> Python backend ------> Web app (React)
               receiver                (visualization)
               parser_handler
               parsers
```
## Supported packets
This is the initial list, the rest of the packets are WIP.

| Id | Packet | Status |
|----|--------|--------|
| 2 | Lap Data | Done |
| 4 | Participants | Done |
| 5 | Car Setups | Done |
| 6 | Car Telemetry | Done |
| 7 | Car Status | Done |
| 8 | Final Classification | Done |

## Game setup
In F1 25, go to **Settings > Telemetry Settings** and set:
| Option | Value |
|--------|-------|
| UDP Telemetry | On |
| UDP Format | 2025 |

## License
This project is licensed under the [GNU General Public License v3.0](LICENSE)
