from app import db


class Stock(db.Model):
    __tablename__ = "stock"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer)
    transaction_date = db.Column(db.String)
    quantity = db.Column(db.Integer)
    in_out = db.Column(db.String(10))

    def __init__(self, product_id, transaction_date, quantity, in_out):
        self.product_id = product_id
        self.transaction_date = transaction_date
        self.quantity = quantity
        self.in_out = in_out
