from app.repositories.stock_repo import StockRepo
from app.models import Stock
from datetime import datetime


class StockService:
    def __init__(self):
        self.stock_repo = StockRepo()

    def make_sale(self, product_id, quantity, transaction_date=None):
        if self.check_quantity(product_id) < quantity:
            return "Insufficient stock"

        if transaction_date is None:
            transaction_date = datetime.now()
        stock = Stock(
            product_id=product_id,
            transaction_date=transaction_date,
            quantity=quantity,
            in_out="out",
        )
        self.stock_repo.save(stock)
        return "Sale made successfully"

    def refuel(self, product_id, quantity, transaction_date=None):
        if transaction_date is None:
            transaction_date = datetime.now()
        stock = Stock(
            product_id=product_id,
            transaction_date=transaction_date,
            quantity=quantity,
            in_out="in",
        )
        self.stock_repo.save(stock)

    def check_quantity(self, product_id):
        stock = self.stock_repo.find_all_by_product_id(product_id)
        quantity = 0
        for item in stock:
            if item.in_out == "in":
                quantity += item.quantity
            else:
                quantity -= item.quantity
        return quantity
