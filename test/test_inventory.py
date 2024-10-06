import unittest
from app import create_app, db
from app.models import Inventario


class InventoryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_inventory(self):
        item = Inventario(
            producto_id=1,
            fecha_transaccion="2024-10-10",
            cantidad=10,
            entrada_salida="entrada",
        )
        db.session.add(item)
        db.session.commit()
        self.assertEqual(item.id, 1)
        self.assertEqual(item.producto_id, 1)
        self.assertEqual(item.fecha_transaccion, "2024-10-10")
        self.assertEqual(item.cantidad, 10)
        self.assertEqual(item.entrada_salida, "entrada")
