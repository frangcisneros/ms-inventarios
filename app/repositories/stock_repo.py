from app import db, cache
from app.models.stock import Stock


class StockRepo:
    def save(self, stock: Stock):
        stock = db.session.add(stock)
        db.session.commit()
        cache.set(f'stock_{stock.id}', stock, timeout=15)
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
        result = cache.get('stocks')

        if result is None:
            result = Stock.query.all()
            cache.set('stocks', result, timeout=15)
            
        return result
