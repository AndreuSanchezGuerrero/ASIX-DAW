import telepot
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Mode per a transformar les comandes del bot de telegram en funcions
def handle(msg):
    global bot
    global chat_id
    global command
    global valor
    chat_id = msg['chat']['id']
    text = msg['text']
    #si el text conte / assignem command
    if text[0] == '/':
        command = text
        valor = ""
    elif text[0] != '/':
        valor = text
    print('Received: %s' % msg)
    main(chat_id, command, valor)


def main(chat_id, command, valor):
    #Cridem a bot per a enviar missatges
    if command == '/on':
        bot.sendMessage(chat_id, "Led encès")
        GPIO.output(18, True)
    elif command == '/off':
        bot.sendMessage(chat_id, "Led apagat")
        GPIO.output(18, False)
    elif command == '/prr':
        if valor == "":
            bot.sendMessage(chat_id, "Introdueix el temps de parpadeig")
        else:
            segons = int(valor)
            bot.sendMessage(chat_id, "Led parpadejant cada " + str(segons) + " segons")
            try :
                while valor != "stop":
                    valor = bot.getUpdates([-1],['text'])
                    GPIO.output(18, True)
                    time.sleep(segons)
                    GPIO.output(18, False)
                    time.sleep(segons)
            except KeyboardInterrupt:
                bot.sendMessage(chat_id, "Led apagat")
                GPIO.output(18, False)
    elif command == '/polsador':
        bot.sendMessage(chat_id, "Polsador activat")
        try:
            while True:
                if GPIO.input(23) == False:
                    bot.sendMessage(chat_id, "Polsador premut")
                    GPIO.output(18, True)
                else:
                    bot.sendMessage(chat_id, "Polsador no premut") 
                    GPIO.output(18, False)
                time.sleep(3)
        except KeyboardInterrupt:
            bot.sendMessage(chat_id, "Polsador desactivat")
            GPIO.output(18, False)
    elif command == '/pwm':
        bot.sendMessage(chat_id, "PWM activat")
        pwm_led = GPIO.PWM(18, 100)
        pwm_led.start(100)
        i = 0
        try:
            while valor !=stop:
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
            bot.sendMessage(chat_id, "PWM desactivat")
            GPIO.output(18, False)
    elif command == '/alarm':
        bot.sendMessage(chat_id, "Alarma activada")
        try:
            while True:
                if GPIO.input(23) == False:
                    bot.sendMessage(chat_id, "Alarma activada")
                    GPIO.output(18, True)
                    time.sleep(0.5)
                    GPIO.output(18, False)
                    time.sleep(0.5)
                else:
                    GPIO.output(18, False)
        except KeyboardInterrupt:
            bot.sendMessage(chat_id, "Alarma desactivada")
            GPIO.output(18, False)
    elif command == '/motor':
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
                if valor == "":
                    bot.sendMessage(chat_id, "Introdueix la direccio del motor (A/B)")
                else:
                    direccio = valor
                    if velocitat == 0:
                        bot.sendMessage(chat_id, "Introdueix la velocitat del motor (0-100)")
                    else:
                        velocitat = int(valor)
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
    elif command == '/exit':
        bot.sendMessage(chat_id, "Surtint...")
        GPIO.cleanup()
        exit()
    elif command == '/help':
        bot.sendMessage(chat_id, "Comandes disponibles:")
        bot.sendMessage(chat_id, "/on: encen el led")
        bot.sendMessage(chat_id, "/off: apaga el led")
        bot.sendMessage(chat_id, "/prr: parpadeja el led cada x segons")
        bot.sendMessage(chat_id, "/polsador: activa el polsador")
        bot.sendMessage(chat_id, "/pwm: activa el pwm")
        bot.sendMessage(chat_id, "/alarm: activa l'alarma")
        bot.sendMessage(chat_id, "/help: mostra les comandes disponibles")
    if valor == "stop":
        bot.sendMessage(chat_id, "Surtint...")
        GPIO.cleanup()
        valor = ""
        exit()

global bot
global chat_id
global command
global valor

bot = telepot.Bot("5971083063:AAGMt8xb5-FlM8kToSlxreo9ow0o1sA3Q-c")
while True:
    time.sleep(1)
    bot.getUpdates(handle)
    print('I am listening ...')

while 1:
    time.sleep(10)