import unittest
from app import create_app, db
from app.models import Stock
from app.services.ms_stock import StockService
from app.repositories.stock_repo import StockRepo


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
        item = Stock(
            product_id=1, transaction_date="2024-10-10", quantity=10, in_out="in"
        )
        db.session.add(item)
        db.session.commit()
        self.assertEqual(item.id, 1)
        self.assertEqual(item.product_id, 1)
        self.assertEqual(item.transaction_date, "2024-10-10")
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.in_out, "in")

    def test_sell_inventory(self):
        ms_stock = StockService()
        ms_stock.make_sale(product_id=1, quantity=10, transaction_date="2024-10-10")
        stock_repo = StockRepo()
        stock = stock_repo.find_by_id(1)
        if stock is not None:
            self.assertEqual(stock.id, 1)
            self.assertEqual(stock.product_id, 1)
            self.assertEqual(stock.transaction_date, "2024-10-10")
            self.assertEqual(stock.quantity, 10)
            self.assertEqual(stock.in_out, "out")

    def test_refuel_inventory(self):
        ms_stock = StockService()
        ms_stock.refuel(product_id=1, quantity=10, transaction_date="2024-10-10")
        stock_repo = StockRepo()
        stock = stock_repo.find_by_id(1)
        if stock is not None:
            self.assertEqual(stock.id, 1)
            self.assertEqual(stock.product_id, 1)
            self.assertEqual(stock.transaction_date, "2024-10-10")
            self.assertEqual(stock.quantity, 10)
            self.assertEqual(stock.in_out, "in")

    def test_item_check_quantity(self):
        ms_stock = StockService()
        ms_stock.refuel(product_id=1, quantity=10, transaction_date="2024-10-10")
        ms_stock.make_sale(product_id=1, quantity=5, transaction_date="2024-10-10")
        quantity = ms_stock.check_quantity(product_id=1)
        print(quantity)
        self.assertEqual(quantity, 5)
