import config
from aliexpress_api import AliexpressApi,models
import random,time

api = AliexpressApi(key=config.app_key,
                    secret=config.app_secret,
                    language=models.Language.EN,
                    currency=models.Currency.USD,
                    tracking_id="default")

def get_products(page_no) -> list[models.Product]:

    categories = config.categories.split(",")
    products   = []
    for category in categories : 
        try : 
            scraped_products = api.get_products(category_ids=category,
                                                page_no=page_no,
                                                page_size=50)
        except Exception as e : 
            continue
        products.extend(scraped_products)
        time.sleep()
    random.shuffle(products)
    return products