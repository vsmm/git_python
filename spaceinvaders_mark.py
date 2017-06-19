from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

X = [0,255,0]  # green
O = [0,0,0]  # black

spinv_mark = [
O,O,O,X,X,O,O,O,
O,O,X,X,X,X,O,O,
O,X,X,X,X,X,X,O,
X,X,O,X,X,O,X,X,
X,X,X,X,X,X,X,X,
O,O,X,O,O,X,O,O,
O,X,O,X,X,O,X,O,
X,O,X,O,O,X,O,X
]

while True:
    sense.set_rotation(270)
    sense.clear()
    sleep(1)
    sense.set_pixels(spinv_mark)
    sleep(1)
    sense.clear()
