from datetime import datetime

class EagyBroker:
    def __init__(self):
        self.initial_prices = {}
        self.current_prices = {}
        self.num_shares_sold = {}
        self.num_shares_bought = {}

    def subscribe(self, stock_exchanger):
        """Subscribes to a Stock Exchanger and store the initial price."""
        share = stock_exchanger.share
        current_price = stock_exchanger.current_price
        self.initial_prices[share], self.current_prices[share] = current_price, current_price
        self.num_shares_sold[share], self.num_shares_bought[share] = 0, 0

    def process_event(self, event):
        """Processes a queue event (price or volume)."""
        share, event_type, *data = event
        if event_type == 'price':
            self.current_prices[share] = data[0]
            print(self.suggest(share))
            self.num_shares_sold[share], self.num_shares_bought[share] = 0, 0
        elif event_type == 'volume':
            self.num_shares_sold[share] += data[0]
            self.num_shares_bought[share] += data[1]

    def suggest(self, share):
        """Suggests an operation."""
        initial_price, current_price = self.initial_prices[share], self.current_prices[share]
        num_shares_sold, num_shares_bought = self.num_shares_sold[share], self.num_shares_bought[share]
        print(
            f"\nnum_shares_sold: {num_shares_sold} num_shares_bought: {num_shares_bought} initial_price: {initial_price} current_price: {current_price}")
        if num_shares_sold > 2000 and current_price <= initial_price * 0.9:
            return f"{datetime.now()} - Eagy Broker suggests to BUY {share}"
        elif num_shares_bought > 2000 and current_price >= initial_price * 1.1:
            return f"{datetime.now()} - Eagy Broker suggests to SELL {share}"
        return f"{datetime.now()} - Eagy Broker suggests to HOLD {share}"
