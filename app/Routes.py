from app import app




@app.route('/')
def home():
    return "Welcome Home"



from app import  user,\
    Emloyee,\
    Mail_template,\
    Mail_transfer,\
    Customer_product_csvdatas,\
    Reviewcsvdata,\
    Orders_csvdata,\
    UserProductList,\
    Filtering


# user.py - User file has the api to manipulate user data

# employee.py - employee file has the api to manipulate employee data and delete user data

# mail_template - file with api for employee to create html template

# mail_transfer - file with api to send mail to list of customers with dynamic template

# customer_product_csvdatas - file with api to upload csv data of user and product to database

# Reviewcsvdata - file with api to upload csv data of review

# orders_csvdata -file with api to upload csv data of orders

# userProductList- file with api to upload csv data of user product list

# Filtering - file with api to filter out customers on certain constraint




