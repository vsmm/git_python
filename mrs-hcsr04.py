import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(18,GPIO.OUT)

GPIO.output(TRIG, False)
while(1):
   
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    dst = int(distance)
    if(dst == 6):
	time.sleep(0.1)	
	GPIO.output(18,1)
	time.sleep(0.1)	
	GPIO.output(18,0)
	time.sleep(0.1)	
	GPIO.output(18,1)
	time.sleep(0.1)	
	GPIO.output(18,0)
#	time.sleep(0.1)	
#    GPIO.output(18,1)
 #   time.sleep(1)	
  #  GPIO.output(18,0)
   
    print "Distance:",distance,"cm"
    print "Distance:",dst,"cm"
    
  #  GPIO.cleanup()
