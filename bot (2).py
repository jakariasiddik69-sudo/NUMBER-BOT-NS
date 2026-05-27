import telebot
import os
import requests
import json
import time
import threading
import pyotp
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

# Render-e Environment Variables theke data nibe
TOKEN = os.environ.get('TOKEN')
NEXA_API_KEY = os.environ.get('NEXA_API_KEY')

bot = telebot.TeleBot(TOKEN)

# CopyTextButton check
try:
    from telebot.types import CopyTextButton
    HAS_COPY_BTN = True
except ImportError:
    HAS_COPY_BTN = False

# Button Style Patch
def ibtn(text, callback_data=None, url=None, style=None, copy_text_str=None):
    kwargs = {'text': text}
    if callback_data: kwargs['callback_data'] = callback_data
    if url: kwargs['url'] = url
    
    btn = InlineKeyboardButton(**kwargs)
    if style: setattr(btn, 'style', style)
    
    if copy_text_str and HAS_COPY_BTN:
        # Modern telebot versions support copy_text
        btn.copy_text = {"text": copy_text_str}
    return btn

# Main logic ekhane thakbe
print("💎 NUMBER BOT NS BOT IS STARTING...")

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
