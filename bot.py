from googletrans import Translator
import googletrans
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

trans = Translator()

bot = telebot.TeleBot("1988972594:AAEu3sugTnTsbSa0uj1oqVwQ4LNGn1-9l2M")

word = "Your selected language is  "

@bot.message_handler(commands=['start'])
def start(msg):
    key = ReplyKeyboardMarkup(True, False)
    key.add("⚙️ Change my language")
    text = "Welcome our translator bot, \nYou can easily translate your words using this bot.\nPress the <code>⚙️ Change my language</code> button to\n select your desired language 👇👇👇"
    bot.send_message(msg.from_user.id, text, reply_markup=key, parse_mode="HTML")

@bot.message_handler(content_types = ['text'])
def text(msg):
    if msg.text == "⚙️ Change my language":
        key = InlineKeyboardMarkup()
        ls = googletrans.LANGUAGES
        for i in range(len(ls, 2)):
            data = i + "_dict"
            btn = InlineKeyboardButton(ls[i], callback_data=data)
            key.add(btn)
        bot.send_message(msg.from_user.id, "Select your language from these:", reply_markup=key)


@bot.callback_query_handler(func=lambda call: True)
def call(call):
    print(call.data)



bot.polling()
    
    

    