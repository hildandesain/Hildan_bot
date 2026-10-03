import os
import telebot
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MY_ID = int(os.getenv("MY_ID", "0"))

bot = telebot.TeleBot(TOKEN)

def is_owner(message):
    if message.from_user.id != MY_ID:
        bot.reply_to(message, "⛔ Private bot punya Hildan aja.")
        return False
    return True

@bot.message_handler(commands=['start','help'])
def start(message):
    if not is_owner(message): return
    bot.reply_to(message, "Halo Bos Hildan! Bot tanpa API udah online ✅\n\n/start - cek bot\nKetik apa aja bakal dijawab.")

@bot.message_handler(func=lambda m: True)
def echo(message):
    if not is_owner(message): return
    t = message.text.lower()
    if "halo" in t or "hai" in t:
        bot.reply_to(message, f"Halo! Jam {datetime.now().strftime('%H:%M')} ada yang bisa dibantu?")
    else:
        bot.reply_to(message, f"Kamu: {message.text}\n\nBot dengerin!")

print("Bot jalan...")
bot.infinity_polling()
