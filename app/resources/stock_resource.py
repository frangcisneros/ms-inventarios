# app/resources/stock_resource.py

from flask import Blueprint, request
from app.models.stock import Stock
from app.repositories.stock_repo import StockRepo
from app.services.ms_stock import StockService

stock_bp = Blueprint("stock", __name__)
stock_service = StockService()


@stock_bp.route("/stock", methods=["GET"])
def index():
    """Endpoint to check stock inventory."""
    return "hola", 200


@stock_bp.route("/stock/refuel", methods=["POST"])
def refuel():
    """Endpoint to refuel stock."""
    data = request.json
    if data is None or "product_id" not in data or "quantity" not in data:
        return "Invalid input", 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")
    stock_service.refuel(product_id, quantity)

    return "Refuel made successfully", 200


@stock_bp.route("/stock/sell", methods=["POST"])
def sell():
    """Endpoint to sell stock."""
    data = request.json
    if data is None or "product_id" not in data or "quantity" not in data:
        return "Invalid input", 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")
    stock_service.make_sale(product_id, quantity)

    return "Sale made successfully", 200


@stock_bp.route("/stock/check_quantity/<int:product_id>", methods=["GET"])
def check_quantity(product_id):
    """Endpoint to check the quantity of a specific product."""
    quantity = stock_service.check_quantity(product_id)
    return {"quantity": quantity}, 200
