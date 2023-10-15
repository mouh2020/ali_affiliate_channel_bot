from controller import *
from config import bot_token,channel_id
from utils import *
from loguru import logger
from telebot import TeleBot
from time import sleep
import json

logger.add("bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="w")

bot = TeleBot(bot_token)

while True : 
    try :
        file = open("conf.json")
        data = json.load(file)
        file.close()
        product = get_products(page_no=1,
                               categories=data["categories"])
        if product_exsits(product_id=product.product_id) : 
            continue
        insert_product(product_id=product.product_id)
        product = build_affiliate_link(product)
        message = build_message(product,data["message"])
        bot.send_photo(chat_id=channel_id,
                    photo=product.product_main_image_url,
                    caption=message)
        logger.info(f"product shared successfully product_id : {product.product_id}")
        logger.info(f"sleep for {data['time']*60} minutes for next share")
        sleep(60*data["time"])

    except Exception as e : 
        logger.error(f"an error occured : {str(e)}")

