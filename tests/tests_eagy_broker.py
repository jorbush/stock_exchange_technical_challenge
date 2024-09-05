import unittest
from queue import Queue
from eagy_broker import EagyBroker
from stock_exchanger import StockExchanger


class TestEagyBroker(unittest.TestCase):
    def setUp(self):
        self.broker = EagyBroker()
        self.queue = Queue()
        self.amzn_exchanger = StockExchanger('AMZN', self.queue)
        self.aapl_exchanger = StockExchanger('AAPL', self.queue)

    def test_subscribe(self):
        """Test that the broker subscribes and stores initial and current prices."""
        self.broker.subscribe(self.amzn_exchanger)
        self.assertIn('AMZN', self.broker.initial_prices)
        self.assertEqual(
            self.broker.initial_prices['AMZN'], self.amzn_exchanger.initial_price)
        self.assertEqual(
            self.broker.current_prices['AMZN'], self.amzn_exchanger.current_price)
        self.assertEqual(self.broker.num_shares_sold['AMZN'], 0)
        self.assertEqual(self.broker.num_shares_bought['AMZN'], 0)

    def test_process_price_event(self):
        """Test that the broker processes price events and updates the current price."""
        self.broker.subscribe(self.amzn_exchanger)
        event = ('AMZN', 'price', 130)
        self.broker.process_event(event)
        self.assertEqual(self.broker.current_prices['AMZN'], 130)

    def test_process_volume_event(self):
        """Test that the broker processes volume events and updates the number of shares sold and bought."""
        self.broker.subscribe(self.amzn_exchanger)
        event = ('AMZN', 'volume', 2100, 2200)
        self.broker.process_event(event)
        self.assertEqual(self.broker.num_shares_sold['AMZN'], 2100)
        self.assertEqual(self.broker.num_shares_bought['AMZN'], 2200)

    def test_suggest_buy(self):
        """Test that the broker suggests to BUY when conditions are met."""
        self.broker.subscribe(self.amzn_exchanger)
        self.broker.initial_prices['AMZN'] = 100
        self.broker.current_prices['AMZN'] = 80
        self.broker.num_shares_sold['AMZN'] = 2100
        suggestion = self.broker.suggest('AMZN')
        self.assertEqual(suggestion, "Eagy Broker suggests to BUY AMZN")

    def test_suggest_sell(self):
        """Test that the broker suggests to SELL when conditions are met."""
        self.broker.subscribe(self.amzn_exchanger)
        self.broker.initial_prices['AMZN'] = 100
        self.broker.current_prices['AMZN'] = 130
        self.broker.num_shares_bought['AMZN'] = 2200
        suggestion = self.broker.suggest('AMZN')
        self.assertEqual(suggestion, "Eagy Broker suggests to SELL AMZN")

    def test_suggest_hold(self):
        """Test that the broker suggests to HOLD when no buy/sell conditions are met."""
        self.broker.subscribe(self.amzn_exchanger)
        self.broker.initial_prices['AMZN'] = 100
        self.broker.current_prices['AMZN'] = 105
        self.broker.num_shares_sold['AMZN'] = 1900
        self.broker.num_shares_bought['AMZN'] = 1950
        suggestion = self.broker.suggest('AMZN')
        self.assertEqual(suggestion, "Eagy Broker suggests to HOLD AMZN")


if __name__ == '__main__':
    unittest.main()
