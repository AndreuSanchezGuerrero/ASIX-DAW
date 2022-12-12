#Mode per a transformar les comandes del bot de telegram en funcions
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' % msg)
    if command == '/on':
        encendreLed()
        bot.sendMessage(chat_id, "Led encès")
    elif command == '/off':
        apagarLed()
        bot.sendMessage(chat_id, "Led apagat")
    elif command == '/pols':
        modepolsador()
        bot.sendMessage(chat_id, "Mode polsador")
    elif command == '/pwm':
        PWM()
        bot.sendMessage(chat_id, "Mode PWM")
    elif command == '/alarm':
        alarma()
        bot.sendMessage(chat_id, "Mode Alarma")
    elif command == '/clear':
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(18, False)
        bot.sendMessage(chat_id, "S'ha netejat el GPIO")
    else:
        bot.sendMessage(chat_id, "Comanda no reconeguda")

def telegraminput(bot):
    print(bot.getMe())
    loop.MessageLoop(bot, handle).run_as_thread()
    print('Listening ...')
    while 1:
        time.sleep(10)