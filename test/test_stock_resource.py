import unittest
from app import create_app, db


class StockResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_ms_stock(self):
        client = self.app.test_client(use_cookies=True)
        response = client.get("http://localhost:5000/api/v1/stock")
        self.assertEqual(response.status_code, 200)

    def test_ms_stock_refuel(self):
        client = self.app.test_client(use_cookies=True)
        response = client.post(
            "http://localhost:5000/api/v1/stock/refuel",
            json={"product_id": 1, "quantity": 10},
        )
        self.assertEqual(response.status_code, 200)

    def test_ms_stock_sell(self):
        client = self.app.test_client(use_cookies=True)
        response = client.post(
            "http://localhost:5000/api/v1/stock/sell",
            json={"product_id": 1, "quantity": 10},
        )
        self.assertEqual(response.status_code, 200)

    def test_ms_check_quantity(self):
        client = self.app.test_client(use_cookies=True)
        response = client.post(
            "http://localhost:5000/api/v1/stock/refuel",
            json={"product_id": 1, "quantity": 10},
        )
        response = client.get("http://localhost:5000/api/v1/stock/check_quantity/1")
        self.assertEqual(response.status_code, 200)
        if response.json is not None:
            self.assertEqual(response.json["quantity"], 10)
