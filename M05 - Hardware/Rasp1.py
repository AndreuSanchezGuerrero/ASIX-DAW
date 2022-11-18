#Fem el codi per a que el led es pari i es torni a encendre cada 3 segons
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(18, True)
    time.sleep(3)
    GPIO.output(18, False)
    time.sleep(3)

GPIO.cleanup()

#Modificar l’esquema anterior per controlar l’estat d’un Led amb un polsador
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(23)
    if input_state == False:
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)
    time.sleep(0.2)

GPIO.cleanup()

#A partir de l’exercici anterior, modificar el guió perquè el led s’encengui gradualment, recordar utilitzar PWM, posar el codi del guió python 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)
p.start(0)
try:
    while True:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()

GPIO.cleanup()
