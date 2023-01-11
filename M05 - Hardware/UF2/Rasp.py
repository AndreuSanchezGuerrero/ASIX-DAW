
import RPi.GPIO as GPIO
import time
import telepot 

#Demanem el chat_id de l'usuari
chat_id = ""
#input("Introdueix el chat_id: ")
#Demanem el token del bot
bot = telepot.Bot("5971083063:AAGMt8xb5-FlM8kToSlxreo9ow0o1sA3Q-c")
#input("Introdueix el token: ")

def encendreLed():
    try:
        GPIO.output(18, True)
    except KeyboardInterrupt:
        menu()

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
        menu()

def PWM():
    pwm_led = GPIO.PWM(18, 100)
    pwm_led.start(100)
    i = 0
    try:
        while True:
            print (i)
            if GPIO.input(23) == False:
                i = i + 1
                if i == 11:
                    i = 10
                pwm_led.ChangeDutyCycle(i)
                time.sleep(0.1)
            else:
                i = i - 1
                if i == -1:
                    i = 0
                pwm_led.ChangeDutyCycle(i)
                time.sleep(0.1)
    except KeyboardInterrupt:
        menu()

def alarma(chat_id,bot):
    if chat_id == "" or bot == "":
        print("No tens el chat_id o el token assignats")
        menu()
    try:
        while True:
            if GPIO.input(23) == False: #Porta Oberta
                bot.sendMessage(chat_id, "Porta Oberta")
                time.sleep(3)
    except KeyboardInterrupt:
        menu()

def motor():
    try:
        M1enable = 17
        M1sentitA = 27
        M1sentitB = 22
        freq_pwm = 100
        velocitat = 0
        GPIO.setup(M1enable, GPIO.OUT)
        GPIO.setup(M1sentitA, GPIO.OUT)
        GPIO.setup(M1sentitB, GPIO.OUT)
        #inicialitzem el PWM
        pwm_motor = GPIO.PWM(M1enable,freq_pwm)
        pwm_motor.start(0)
        #Preguntem cap a on volem que vagi el motor
        direccio=input("Cap a on vols que vagi el motor? (A/B): ")
        #Preguntem la velocitat
        velocitat=int(input("Quina velocitat vols que vagi el motor? (0-100): "))
        while True:
            try:
                if direccio=="A":
                    print("Forward")
                    GPIO.output(M1sentitA,GPIO.HIGH)
                    GPIO.output(M1sentitB,GPIO.LOW)
                elif direccio=="B":
                    print("Backward")                    
                    GPIO.output(M1sentitA,GPIO.LOW)
                    GPIO.output(M1sentitB,GPIO.HIGH)
                else:
                    print("Direction incorrect")
                    motor()
                pwm_motor.start(velocitat)
            except KeyboardInterrupt:
                print("Stopped")
                GPIO.output(M1sentitA,GPIO.LOW)
                GPIO.output(M1sentitB,GPIO.LOW)
                pwm_motor.stop()
                motor()
    except KeyboardInterrupt:
        menu()

#Fem el menu
def menu():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("1. Encendre led")
    print("2. Apagar led")
    print("3. Parpadejar led")
    print("4. PolSador")
    print("5. PWM")
    print("6. Alarma")
    print("7. Motor")
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
        alarma(chat_id,bot)
    elif opcio == 7:
        motor()
    elif opcio == 8:
        GPIO.cleanup()
        exit()
    else:
        print("Opcio incorrecta")
        menu()

#Fem el bucle per a que el menu es torni a repetir
while True:
    menu()