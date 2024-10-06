from app.repositories.stock_repo import StockRepo
from app.models import Stock
from datetime import datetime


class StockService:
    def __init__(self):
        self.stock_repo = StockRepo()

    def make_sale(self, product_id, quantity, transaction_date=None):
        if transaction_date is None:
            transaction_date = datetime.now()
        stock = Stock(
            product_id=product_id,
            transaction_date=transaction_date,
            quantity=quantity,
            in_out="out",
        )
        self.stock_repo.save(stock)
