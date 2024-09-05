import unittest
from eagy_broker import EagyBroker

class TestEagyBroker(unittest.TestCase):
    def setUp(self):
        self.broker = EagyBroker()

    def test_buy_suggestion(self):
        suggestion = self.broker.suggest("AMZN", 2100, 1900, 100, 89)
        self.assertEqual(suggestion, "Eagy Broker suggests to BUY AMZN")

    def test_sell_suggestion(self):
        suggestion = self.broker.suggest("AMZN", 1900, 2100, 100, 111)
        self.assertEqual(suggestion, "Eagy Broker suggests to SELL AMZN")

    def test_hold_suggestion(self):
        suggestion = self.broker.suggest("AMZN", 1900, 1900, 100, 105)
        self.assertEqual(suggestion, "Eagy Broker suggests to HOLD AMZN")

if __name__ == '__main__':
    unittest.main()
