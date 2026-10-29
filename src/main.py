from gpiozero import MotionSensor
from datetime import datetime

pir = MotionSensor(17)

print("Охорона увімкнена...")
while True:
    pir.wait_for_motion()
    print(f"{datetime.now():%H:%M:%S} Рух виявлено!")
    pir.wait_for_no_motion()
