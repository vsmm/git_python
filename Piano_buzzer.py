import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

#frecuencias
cL = 129
cLS = 139
dL = 146
dLS = 156
eL = 163
fL = 173
fLS = 185
gL = 194
gLS = 207
aL = 219
aLS = 228
bL = 232
c = 261
cS = 277
d = 294
dS = 311
e = 329
f = 349
fS = 370
g = 391
gS = 415
a = 440
aS = 455
b = 466
cH = 523
cHS = 554
dH = 587
dHS = 622
eH = 659
fH = 698
fHS = 740
gH = 784
gHS = 830
aH = 880
aHS = 910
bH = 933
i = 0
#esta funcion es para hacer la onda cuadrada de la senial que el buzzer usa
def beep(nota, duracion):
    #esto es el semi-periodo de cada nota
    beepDelay = 1000000/nota
    #esto es cuanto tiempo necesitamos gastar en la nota
    tiempo = ((duracion*1000)/(beepDelay*2))
    beepdelaymicrosegundo = beepDelay/1000000

    while i < tiempo:
        GPIO.output(17,1)
        sleep(beepDelay)
        #2do semi-periodo
        GPIO.output(17,0)
        sleep(beepDelay)
        i + i + 1

    GPIO.output(17,0)
    sleep(0.02)

def play():
    beep(a,500)
    beep(a,500)
    beep(f,350)
    beep(cH,150)

    beep(a,500)
    beep(f,350)
    beep(cH,150)
    beep(a,1000)
    beep(eH,500)

    beep(eH,500)
    beep(eH,500)
    beep(fH,350)
    beep(cH,150)
    beep(gS,500)

    beep(f,350)
    beep(cH,150)
    beep(a,1000)
    beep(aH,500)
    beep(a,350)

    beep(a,150)
    beep(aH,500)
    beep(gHS,250)
    beep(gH,250)
    beep(fHS,125)

    beep(fH,125)
    beep(fHS,250)

    sleep(0.25)

    beep(aS,250)
    beep(dHS,500)
    beep(dH,250)
    beep(cHS,250)
    beep(cH,125)

    beep( b,125)
    beep( cH,250)

    sleep(0.25)

    beep(f,125)
    beep(gS,500)
    beep(f,375)
    beep(a,125)
    beep(cH,500)

    beep(a,375)
    beep(cH,125)
    beep(eH,1000)
    beep(aH,500)
    beep(a,350)

    beep(a,150)
    beep(aH,500)
    beep(gHS,250)
    beep(gH,250)
    beep(fHS,125)

    beep(fH,125)
    beep(fHS,250)

    sleep(0.25)

    beep(aS,250)
    beep(dHS,500)
    beep(dH,250)
    beep(cHS,250)
    beep(cH,125)

    beep(b,125)
    beep(cH,250)

    sleep(0.25)

    beep(f,250)
    beep(gS,500)
    beep(f,375)
    beep(cH,125)
    beep(a,500)

    beep(f,375)
    beep(c,125)
    beep(a,1000)
try:
    play()


finally:
    GPIO.cleanup()
