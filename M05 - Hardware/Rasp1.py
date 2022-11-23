#Fem el codi per a que el led es pari i es torni a encendre cada 3 segons
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def encendreLed():
    GPIO.output(18, True)

def apagarLed():
    GPIO.output(18, False)

def parpadejarLed():
    try :
        while True:
            GPIO.output(18, True)
            time.sleep(3)
            GPIO.output(18, False)
            time.sleep(3)
    except KeyboardInterrupt:
        GPIO.output(18, False)
        menu()

def modepolsador():
    try:
        while True:
            if GPIO.input(23) == False:
                print("Polsador premut")
                GPIO.output(18, True)
            else:
                print("Polsador no premut") 
                GPIO.output(18, False)
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.output(18, False)
        menu()


#A partir de l’exercici anterior, modificar el guió perquè el led s’encengui gradualment, recordar utilitzar PWM, posar el codi del guió python 
def PWM():
    pwm_led = GPIO.PWM(18, 100)
    pwm_led.start(100)
    i = 0
    try:
        while GPIO.input(23) == True:
            i = i + 1
            pwm_led.ChangeDutyCycle(i)
            time.sleep(0.1)
        else:
            i = i - 1
            pwm_led.ChangeDutyCycle(i)
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.output(18, False)
        menu()

#Simular una alarma amb un polsador, que equivaldria a un sensor de control d’estat d’una porta(oberta o tancada) i que quan la porta estigui oberta envií un telegram, mutt, avisant que la porta s’ha obert. 
def alarma():
    try:
        while True:
            if GPIO.input(23) == False:
                print("Polsador premut")
                GPIO.output(18, True)
                os.system("mutt -s 'Porta oberta' -a /home/pi/Desktop/alarma.txt --")
            else:
                print("Polsador no premut") 
                GPIO.output(18, False)
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.output(18, False)
        menu()

#Fem el menu
def menu():
    print("1. Encendre led")
    print("2. Apagar led")
    print("3. Parpadejar led")
    print("4. PolSador")
    print("5. PWM")
    print("6. Alarma")
    print("8. Sortir")
    opcio = int(input("Tria una opcio: "))
    if opcio == 1:
        encendreLed()
    elif opcio == 2:
        apagarLed()
    elif opcio == 3:
        parpadejarLed()
    elif opcio == 4:
        modepolsador()
    elif opcio == 5:
        PWM()
    elif opcio == 6:
        alarma()
    elif opcio == 8:
        GPIO.cleanup()
        exit()
    else:
        print("Opcio incorrecta")
        menu()

#Fem el bucle per a que el menu es torni a repetir
while True:
    menu()
