import telebot
import math
from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Russia

owm = OWM("86881d9365808609a21eeb824859d89b")
mgr = owm.weather_manager()

bot = telebot.TeleBot("5260271606:AAHYLKrOkahFyphDxVzZ9qV3tseWSvMTeuo")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, в каком ты городе?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    
    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе " + str(math.ceil(temp)) + "\n\n"
    if temp < 10:
        answer += "Сейчас ппц как холодно, одевайся как танк!"
    elif temp < 20:
        answer += "Сейчас холодно, приоденься потеплее."
    bot.send_message(message.chat.id, answer)
bot.infinity_polling()
