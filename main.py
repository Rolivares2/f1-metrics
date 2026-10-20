from receiver import UDPReceiver
from parser_handler import parser_handler
from constants import PacketId

receiver = UDPReceiver()

try:
    for data in receiver.packets():
        decoded = parser_handler(data)
        if decoded is None:
            continue

        packet_id, payload = decoded

except KeyboardInterrupt:
    pass
finally:
    receiver.close()