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
    bot.reply_to(message, """أهلا بك في البوت الخاص بإرسال العروض إلى القناة 

لتغيير الوقت يرجى إرساله على الشكل  time:30

لتعيير الأصناف يرجى إرسالها على الشكل  cat:3,7,52

لتغيير تصميم الرسالة يرجى إرسالها على الشكل design:message""")

@bot.message_handler(commands=['info'])
def info_message(message):
    data = file_operations()
    text = f"الوقت : {data['time']}\n\n الأصناف : {data['categories']}\n\n تصميم الرسالة : \n {data['message']}"
    bot.reply_to(message,
                 text)
    
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