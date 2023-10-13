from googletrans import Translator
import os
from dotenv import load_dotenv
import telebot
from telebot import types

from data_manager import read_text, write_text


load_dotenv()

TELEGRAM_TOKEN = os.getenv("token")


bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    """Кнопки."""
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("en => ru")
    btn2 = types.KeyboardButton("ru => en")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, "Выберите язык:", reply_markup=markup)
    bot.register_next_step_handler(message, language_selection)


def language_selection(message):
    """Выбор языка."""
    if message.text == "en => ru":
        write_text("en ru")
        bot.send_message(message.chat.id, "с английского на русский")
    if message.text == "ru => en":
        write_text("ru en")
        bot.send_message(message.chat.id, "с русского на английский")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    """Получаем сообщение."""
    last_message = message.text
    src, dest = read_text()
    text = translate_text(last_message, src=src, dest=dest)
    bot.send_message(message.chat.id, text)


def translate_text(text, src="ru", dest="en"):
    """Переводим."""
    translator = Translator()
    result = translator.translate(text=text, src=src, dest=dest)
    return result.text


bot.polling(none_stop=True)
