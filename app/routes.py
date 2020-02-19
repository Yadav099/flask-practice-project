from app import app




@app.route('/')
def home():
    return "Welcome Home"


from app import user,emloyee,mail_template,mail_transfer,customer_product_csvdatas,productcsv,orders_csvdata,userProductList,Review