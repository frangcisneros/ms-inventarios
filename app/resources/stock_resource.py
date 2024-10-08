from flask import Blueprint, request
from app.models.stock import Stock
from app.repositories.stock_repo import StockRepo
from app.services.ms_stock import StockService

stock_bp = Blueprint("stock", __name__)
stock_service = StockService()


@stock_bp.route("/stock", methods=["GET"])
# agregar documentacion
def index():
    # agregar inventario index
    return "hola", 200


@stock_bp.route("/stock/refuel", methods=["POST"])
def refuel():
    data = request.json
    if data is None:
        return "Invalid input", 400
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    stock_service.refuel(product_id, quantity)
    return "Refuel made successfully", 200


@stock_bp.route("/stock/sell", methods=["POST"])
def sell():
    data = request.json
    if data is None:
        return "Invalid input", 400
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    stock_service.make_sale(product_id, quantity)
    return "Sale made successfully", 200


@stock_bp.route("/stock/check_quantity/<int:product_id>", methods=["GET"])
def check_quantity(product_id):
    quantity = stock_service.check_quantity(product_id)
    return {"quantity": quantity}, 200
