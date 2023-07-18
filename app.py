from flask import Flask
from controllers.orders_controller import orders_blueprint


app = Flask(__name__)
app.register_blueprint(orders_blueprint)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"