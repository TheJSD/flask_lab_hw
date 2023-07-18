from flask import Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)
order_blueprint = Blueprint("order", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", title="Orders List", order_list = orders)

@order_blueprint.route('/order/<index>')
def order(index):
    specific_order = orders[index - 1]
    return render_template("order.html", title=f"Order: {index}", specific_order = specific_order)