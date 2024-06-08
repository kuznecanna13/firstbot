from config import token
from random import choice
from telebot.types import ReactionTypeEmoji


import telebot


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет")


@bot.message_handler(commands=['joke'])
def joke_handler(message):
    joke = choice(["змея споткнулась", "купил мужик шляпу, а она ему как раз. купил вторую, а она ему как два", "в семье гопников растут три дочери: алёна, тычёна и ващена", "шел медведь по лесу, видит - машина горит. сел в неё и сгорел", "почему маленький дракула не вернулся из школы? ему поставили кол"])
    bot.reply_to(message, joke)


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(func=lambda message: True)
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E"] 
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(choice(emo))], is_big=False)

bot.infinity_polling()