from flask import Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", title="Orders List", order_list = orders)

@orders_blueprint.route('/orders/<index>')
def order(index):
    specific_order = orders[int(index) - 1]
    return render_template("order.html", title=f"Order: {index}", specific_order = specific_order)