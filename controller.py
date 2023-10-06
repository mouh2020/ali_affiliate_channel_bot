from tinydb import TinyDB,Query

db = TinyDB("database.json")

def product_exsits(product_id) : 
    fetched_product = Query()
    product_existance = db.search(fetched_product.id == product_id)
    if len(product_existance) != 0 : 
        return True
    
def insert_product(product_id) : 
    new_product = {'id' : product_id}
    db.insert(new_product)     

