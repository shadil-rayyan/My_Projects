import telebot
from telebot.types import BotDescription,nest1_keyboardButton, ReplyKeyboardMarkup
bot = telebot.TeleBot('')
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(('Annocement'))
    keyboard.row(('Departement'))
    keyboard.row(('Academic calender'))
    keyboard.row(('KTU credit calculator'))
    keyboard.row(('Scholorship'))
    keyboard.row(('Whatsapp'),('contribute'))
    keyboard.row(('Contact us'))
    keyboard.row(('other bots'))
    bot.send_message(message.chat.id, '', reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == "Annocement")
def Annocement_selected(message):
    bot.send_message(message.chat.id, 'coming soon')
    
@bot.message_handler(func=lambda message: message.text == "Departement")
def Departement_selected(message):
    nest1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    nest1_keyboard.row(('CSE'), ('ECE'))
    nest1_keyboard.row(('EEE'), ('IT'))
    nest1_keyboard.row(('CIVIL'), ('MECH'))
    bot.send_message(message.chat.id, '', reply_markup=nest1_keyboard)

#@bot.message_handler(func=lambda message: message.text == "CSE")

# from here academic calender starts
@bot.message_handler(func=lambda message: message.text == "Academic calender")
def Academic_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "KTU credit calculator'")
def ktucredit_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "Scholorship")
def Scholorship_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "contribute")
def contribute_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "Whatsapp")
def whatsapp_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "Other bots")
def otherbot_selected(message):
     bot.send_message(message.chat.id, 'coming soon')
