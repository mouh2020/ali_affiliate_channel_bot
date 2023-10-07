from tinydb import TinyDB,Query
from loguru import logger

logger.add("bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="a")

db = TinyDB("database.json")

def product_exsits(product_id) : 
    logger.info(f"check existance of product_id : {product_id}")
    fetched_product = Query()
    product_existance = db.search(fetched_product.id == product_id)
    if len(product_existance) != 0 : 
        logger.info(f"product exists product_id : {product_id}")
        return True
    logger.info(f"there is no product_id : {product_id}")
    
def insert_product(product_id) : 
    logger.info(f"insert product to databse product_id : {product_id}")
    new_product = {'id' : product_id}
    db.insert(new_product)     

