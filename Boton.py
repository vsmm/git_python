import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,0)

contador = 0

try:
    while contador <= 15:
        if GPIO.input(27):
            GPIO.output (17, 1)
            #contador = contador + 1
            #print 'Contador:', contador
        else:
            GPIO.output(17,0)
            sleep(0.1)
    contador = contador + 1
    print
finally:
    GPIO.cleanup()
