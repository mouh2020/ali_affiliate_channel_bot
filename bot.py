#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot,json
from config import bot_token

bot = telebot.TeleBot(bot_token)

def file_operations(data=None):
    if data : 
        with open("conf.json","w") as file : 
            json.dump(data,file)
            file.close()
        return
    file = open("conf.json")
    data = json.load(file)
    file.close()
    return data

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """بوت التحكم في إرسال العروض إلى قناتك \n\n  لتحديد وقت النشر أرسل time ثم الوقت \n\n  لإرسال التصنيفات أرسلها على الشكل 25,151,159 -\n-""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    try : 
        config  = file_operations()
        changed_data = message.text.split(":")[1]
        if message.text.startswith("design") : 
            config["message"] = ":".join(message.text.split(":")[1:])
        elif message.text.startswith("time") :
            config["time"] = float(changed_data.strip())
        elif message.text.startswith("cat") :
            config["categories"] = changed_data.strip()
        file_operations(config)
        bot.reply_to(message, "تم تغيير المعلومات بنجاح")
    except Exception as e : 
        bot.reply_to(message, "حدث مشكل أثناء تغغير المعلومات")


bot.infinity_polling()