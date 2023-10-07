from controller import *
from config import bot_token,channel_id,interval
from utils import *
from loguru import logger
from telebot import TeleBot
from time import sleep

logger.add("bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="w")

bot = TeleBot(bot_token)


for index,_ in enumerate(range(50),start=1) :
    products = get_products(page_no=index)
    for product in products : 
        if product_exsits(product_id=product.product_id) : 
            continue
        insert_product(product_id=product.product_id)
        product = build_affiliate_link(product)
        message = build_message(product)
        bot.send_photo(chat_id=channel_id,
                       photo=product.product_main_image_url,
                       caption=message)
        sleep(int(interval))