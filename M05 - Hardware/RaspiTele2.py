import sys
import time
import telepot
import telepot.helper
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import (
    per_chat_id, create_open, pave_event_space, include_callback_query_chat_id)
import RPi.GPIO as GPIO

#Repetim el codi anterior pero utilitzant classes

class RaspiTele(telepot.helper.ChatHandler):
    keyboard1 = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Encendre', callback_data='on'),
        InlineKeyboardButton(text='Apagar', callback_data='off'),
        InlineKeyboardButton(text='Parpadejar', callback_data='prr'),
    ],[
        InlineKeyboardButton(text='Polsador', callback_data='polsador'),
        InlineKeyboardButton(text='PWM', callback_data='pwm'),
        InlineKeyboardButton(text='Motor', callback_data='motor'),
    ],[
        InlineKeyboardButton(text='Alarma', callback_data='alarm'),
        InlineKeyboardButton(text='Netejar', callback_data='netejar'),
        InlineKeyboardButton(text='Ajuda', callback_data='ajuda'),
    ]])
    
    keyboardprr = InlineKeyboardMarkup(inline_keyboard=[
        InlineKeyboardButton(text='1s', callback_data='1s'),
        InlineKeyboardButton(text='2s', callback_data='2s'),
        InlineKeyboardButton(text='3s', callback_data='5s'),
    ])
    
    keyboardmotor = InlineKeyboardMarkup(inline_keyboard=[
        InlineKeyboardButton(text='A', callback_data='A'),
        InlineKeyboardButton(text='B', callback_data='B'),
    ])
    
    keyboardstop = InlineKeyboardMarkup(inline_keyboard=[
        InlineKeyboardButton(text='Stop', callback_data='stop'),
    ])

    def __init__(self, *args, **kwargs):
        super(RaspiTele, self).__init__(*args, **kwargs)
        self._count = 0

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print ('Chat:', content_type, chat_type, chat_id)
        print ('Message:', msg)
        self.sender.sendMessage("Benvingut al bot de Raspberry Pi", reply_markup=self.keyboard)
        
    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        print ('Callback Query:', query_id, from_id, query_data)
        self.sender.sendMessage("Has premut el botó: " + query_data)
        if query_data == 'on':
            GPIO.output(18, True)
        elif query_data == 'off':
            GPIO.output(18, False)
        elif query_data == 'prr':
            #hem de demanar el valor de cada cuants segons parpadeja el led i despres fer q parpadeji
            self.sender.sendMessage("Quants segons vols que parpadeji?", reply_markup=self.keyboardprr)
            while True:
                GPIO.output(18, True)
                time.sleep(1)
                GPIO.output(18, False)
                time.sleep(1)
                self.sender.sendMessage(reply_markup=self.keyboardstop)
                if query_data == 'stop':
                    break
        else:
            self.sender.sendMessage("No reconec el botó: " + query_data)
        self.sender.sendMessage("Has premut el botó: " + query_data)
        self.sender.sendMessage("Benvingut al bot de Raspberry Pi", reply_markup=self.keyboard1)
    
    def on__idle(self, event):
        self.sender.sendMessage('Idling')
        self.close
    
    def on_close(self, ex):
        print ('Closed:', ex)
        
#Configuració dels pins de la Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Configuració del bot de Telegram
TOKEN = "5971083063:AAGMt8xb5-FlM8kToSlxreo9ow0o1sA3Q-c"

bot = telepot.DelegatorBot('TOKEN', [
    include_callback_query_chat_id(
        pave_event_space())(
            per_chat_id(), create_open, RaspiTele, timeout=10),
])

MessageLoop(bot).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)