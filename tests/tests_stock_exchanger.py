import unittest
from stock_exchanger import StockExchanger


class TestStockExchanger(unittest.TestCase):
    def setUp(self):
        self.exchanger = StockExchanger("AMZN")

    def test_initial_price_range(self):
        initial_price = self.exchanger.get_initial_price()
        self.assertGreaterEqual(initial_price, 80)
        self.assertLessEqual(initial_price, 120)

    def test_broadcast_ranges(self):
        current_price, num_shares_sold, num_shares_bought = self.exchanger.broadcast()
        self.assertGreaterEqual(current_price, 60)
        self.assertLessEqual(current_price, 140)
        self.assertGreaterEqual(num_shares_sold, 1800)
        self.assertLessEqual(num_shares_sold, 2200)
        self.assertGreaterEqual(num_shares_bought, 1800)
        self.assertLessEqual(num_shares_bought, 2200)


if __name__ == '__main__':
    unittest.main()
