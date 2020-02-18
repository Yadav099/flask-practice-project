from app import app




@app.route('/')
def home():
    return "Welcome Home"


from app import user,emloyee,mail_template