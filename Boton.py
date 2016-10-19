import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.input(27,0)
GPIO.output(17,0)

contador = 0

try:
    while True:
        if (GPIO.input(27)== 1):
            GPIO.output (17, 1)
            contador = contador + 1
            print 'Contador:', contador
        else:
            GPIO.output(17,0)

finally:
    GPIO.cleanup()
