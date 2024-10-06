from app import db
from app.models.stock import Stock


class StockRepo:
    def save(self, stock: Stock):
        db.session.add(stock)
        db.session.commit()
        return stock

    def find_by_id(self, id):
        return Stock.query.filter_by(id=id).first()
