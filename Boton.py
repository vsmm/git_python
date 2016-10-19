import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,0)

contador = 0

try:
    while True:
        GPIO.output(17, GPIO.input(27))

        if (GPIO.input(27) == 1):
            GPIO.output (17, 1)
            contador = contador + 1
            #print 'Contador:', contador
        else
            GPIO.output(17,0)

except KeyboardInterrupt:
    GPIO.cleanup()
