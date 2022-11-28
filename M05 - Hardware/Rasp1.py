#Fem el codi per a que el led es pari i es torni a encendre cada 3 segons
import RPi.GPIO as GPIO
import time
import telepot as tp
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
bot = tp.Bot('5971083063:AAGMt8xb5-FlM8kToSlxreo9ow0o1sA3Q-c') 

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
        while True:
            print (i)
            if GPIO.input(23) == True:
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
        GPIO.output(18, False)
        menu()

#Simular una alarma amb un polsador, que equivaldria a un sensor de control d’estat d’una porta(oberta o tancada) i que quan la porta estigui oberta envií un telegram, mutt, avisant que la porta s’ha obert. 
def alarma():
    try:
        while True:
            if GPIO.input(23) == False: #Porta Oberta
                bot.sendMessage(668520827,'Porta Oberta')
                time.sleep(3)
    except KeyboardInterrupt:
        GPIO.output(18, False)
        menu()

#Mode per a transformar les comandes del bot de telegram en funcions
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' % msg)
    if command == 'on':
        encendreLed()
        bot.sendMessage(chat_id, "Led encès")
    elif command == 'off':
        apagarLed()
        bot.sendMessage(chat_id, "Led apagat")

def telegram():
    bot.message_loop(handle)
    print(bot.getMe())
    MessageLoop(bot, handle).run_as_thread()
    print('Listening ...')
    while 1:
        time.sleep(10)

#Fem el menu
def menu():
    print("1. Encendre led")
    print("2. Apagar led")
    print("3. Parpadejar led")
    print("4. PolSador")
    print("5. PWM")
    print("6. Alarma")
    print("7. Telegram")
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
    elif opcio == 7:
        telegram()
    elif opcio == 8:
        GPIO.cleanup()
        exit()
    else:
        print("Opcio incorrecta")
        menu()

#Fem el bucle per a que el menu es torni a repetir
while True:
    menu()
