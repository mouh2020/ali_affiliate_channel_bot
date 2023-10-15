import config
from aliexpress_api import AliexpressApi,models
import random
from loguru import logger

logger.add("bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="a")

api = AliexpressApi(key=config.app_key,
                    secret=config.app_secret,
                    language=models.Language.EN,
                    currency=models.Currency.USD,
                    tracking_id="default")

def get_products(page_no,categories) -> list[models.Product]:
    products   = []
    for category in categories : 
        logger.info(f"fetch products for category : {category}")
        try : 
            scraped_products = api.get_products(category_ids=categories,
                                                page_no=page_no,
                                                page_size=50)
        except Exception as e : 
            logger.info(f"no products for category : {category}")
            continue
        logger.info(f"{len(scraped_products)}  fetched products for category : {category}")
        products.extend(scraped_products)
    return random.choice(products)

def build_affiliate_link(product: models.Product):
    logger.info(f"build affiliate link for product_id : {product.product_id}")
    affilate_link = api.get_affiliate_links(product.promotion_link)[0].promotion_link
    product.promotion_link = affilate_link 
    return product

def build_message(product: models.Product,message) : 
    logger.info(f"build message product for product_id : {product.product_id}")
    message = message.replace("title",product.product_title)
    message = message.replace("link",product.promotion_link)
    message = message.replace("price",product.target_sale_price)
    return message