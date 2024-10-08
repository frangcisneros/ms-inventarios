from flask import Blueprint, request
from app.models.stock import Stock
from app.repositories.stock_repo import StockRepo
from app.services.ms_stock import StockService

stock_bp = Blueprint("stock", __name__)


@stock_bp.route("/stock", methods=["GET"])

# agregar documentacion


def index():
    # agregar inventario index
    return "hola"
