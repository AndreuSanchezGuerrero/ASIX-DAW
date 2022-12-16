import telepot
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Mode per a transformar les comandes del bot de telegram en funcions
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' % msg)
    main(chat_id, command)

def main(chat_id, command):
    #Cridem a bot per a enviar missatges
    value = bot.getUpdates()
    if command == '/on':
        bot.sendMessage(chat_id, "Led encès")
        GPIO.output(18, True)
    elif command == '/off':
        bot.sendMessage(chat_id, "Led apagat")
        GPIO.output(18, False)
    elif command == '/prr':
        bot.sendMessage(chat_id, "Introdueix el temps de parpadeig")
        segons = bot.getUpdates()
        bot.sendMessage(chat_id, "Led parpadejant")
        try :
            while True:
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
            bot.sendMessage(chat_id, "PWM desactivat")
            GPIO.output(18, False)

global bot

bot = telepot.Bot("5971083063:AAGMt8xb5-FlM8kToSlxreo9ow0o1sA3Q-c")
bot.message_loop(handle)
print('I am listening ...')

while 1:
    time.sleep(10)