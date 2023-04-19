import datetime
import telebot
from telebot import types
from telebot.types import Message
from config import DEFAULT_COMMANDS

bot = telebot.TeleBot('6059217618:AAGyLyhn8sqKwBjpEP0szoUyvaObN0D9ds0')


@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}, wanna check your skill, press SPEED' )

@bot.message_handler(commands=['speed'])
def bot_speed(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton('yes')
    no = types.KeyboardButton('no')
    markup.row(yes, no)
    msg = bot.send_message(message.from_user.id, 'if are u ready, press YES and lets go!!!', reply_markup=markup)
    bot.register_next_step_handler(msg, yess)

def yess(message):
    if message.text == 'yes':
        with open('text.txt', 'r') as file:
            text = file.read()
            start = datetime.datetime.now()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            stop = types.KeyboardButton('stop')
            markup.row(stop)
            msg = bot.send_message(message.from_user.id, text, reply_markup=markup)
            bot.register_next_step_handler(msg, stoped, start)
    else:
        bot.reply_to(message, f'Dont waste my time, {message.from_user.first_name}. Press SPEED or get out of here! ')


def stoped(message, start):
    if message.text == 'stop':
        end = datetime.datetime.now()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('u should check the reviews out', url='https://megalife.by/otzivy'))
        bot.send_message(message.from_user.id, f'{end - start}', reply_markup=markup)








@bot.message_handler(commands=['help'])
def bot_help(message):
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, '\n'.join(text))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.reply_to(message, f'Dont waste my time, {message.from_user.first_name}. Press START or get out of here! ')
bot.polling(none_stop=True, interval=0)
