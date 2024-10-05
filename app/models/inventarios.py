from app import db


class Inventarios(db.Model):
    __tablename__ = "inventarios"
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))
    fecha_transaccion = db.Column(db.DateTime)
    cantidad = db.Column(db.Integer)
    entrada_salida = db.Column(db.Integer)
