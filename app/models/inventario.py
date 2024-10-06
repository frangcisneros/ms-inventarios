from app import db


class Inventario(db.Model):
    __tablename__ = "inventario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto_id = db.Column(db.Integer)
    fecha_transaccion = db.Column(db.String)
    cantidad = db.Column(db.Integer)
    entrada_salida = db.Column(db.String(10))

    def __init__(self, producto_id, fecha_transaccion, cantidad, entrada_salida):
        self.producto_id = producto_id
        self.fecha_transaccion = fecha_transaccion
        self.cantidad = cantidad
        self.entrada_salida = entrada_salida
