from flask import Blueprint, jsonify, request
from app.models.stock import Stock
from app.repositories.stock_repo import StockRepo
from app.services.ms_stock import StockService

stock_bp = Blueprint("stock", __name__)
stock_service = StockService()
stock_repo = StockRepo()


@stock_bp.route("/stock", methods=["GET"])
def index():
    """Endpoint to check stock inventory."""
    return jsonify({"message": "hola"}), 200


@stock_bp.route("/stock/get_all", methods=["GET"])
def get_stock():
    stock = stock_repo.all()
    return jsonify(
        [
            {
                "id": item.id,
                "product_id": item.product_id,
                "transaction_date": item.transaction_date,
                "quantity": item.quantity,
                "in_out": item.in_out,
            }
            for item in stock
        ]
    )


@stock_bp.route("/stock/refuel", methods=["POST"])
def refuel():
    """Endpoint to refuel stock."""
    data = request.json
    if data is None or "product_id" not in data or "quantity" not in data:
        return jsonify({"message": "Invalid input"}), 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")
    stock_service.refuel(product_id, quantity)

    return jsonify({"message": "Refuel made successfully"}), 200


@stock_bp.route("/stock/sell", methods=["POST"])
def sell():
    """Endpoint to sell stock."""
    data = request.json
    if data is None or "product_id" not in data or "quantity" not in data:
        return jsonify({"message": "Invalid input"}), 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")
    message = stock_service.make_sale(product_id, quantity)

    return jsonify({"message": message}), 200


@stock_bp.route("/stock/check_quantity/<int:product_id>", methods=["GET"])
def check_quantity(product_id):
    """Endpoint to check the quantity of a specific product."""
    quantity = stock_service.check_quantity(product_id)
    if quantity == 0:
        return jsonify({"quantity": quantity}), 409
    else:
        return jsonify({"quantity": quantity}), 200


@stock_bp.route("/stock/delete_product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Endpoint to delete a product."""
    stock_service.delete_product(product_id)
    return jsonify({"message": "Product deleted successfully"}), 200
