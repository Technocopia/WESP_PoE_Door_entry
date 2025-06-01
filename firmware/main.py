import machine
import time
from wiegand import WiegandDecoder
from doorstrike import DoorStrike

# setup  
strikes = [
    DoorStrike(machine.Pin(13,machine.Pin.OUT),polarity=False),
    DoorStrike(machine.Pin(18,machine.Pin.OUT),polarity=False)
    ]



wiegand = WiegandDecoder(
            machine.Pin(35,machine.Pin.IN),
            machine.Pin(34,machine.Pin.IN))

print(wiegand)
while True:
    time.sleep(0.1)
    if wiegand.has_scanned_code():
        print("Code!")
        code = wiegand.get_scanned_code()
        print()
        print(f"{code}")
        for s in strikes:
            print(s)
            s.open_door()
            time.sleep(1)

    else:
        print(".",end='')