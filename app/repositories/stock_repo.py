from app import db
from app.models.stock import Stock


class StockRepo:
    def save(self, stock: Stock):
        db.session.add(stock)
        db.session.commit()
        return stock

    def find_by_id(self, id):
        return Stock.query.filter_by(id=id).first()

    def find_all_by_product_id(self, product_id):
        return Stock.query.filter_by(product_id=product_id).all()

    def delete(self, stock: Stock):
        db.session.delete(stock)
        db.session.commit()
        return stock

    def all(self):
        return Stock.query.all()
