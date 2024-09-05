from random import randint

class StockExchanger:
    def __init__(self, share):
        self.share = share
        self.initial_price = randint(80, 120)
        self.current_price = self.initial_price
        self.num_shares_sold = 0
        self.num_shares_bought = 0

    def broadcast(self):
        self.current_price = randint(60, 140)
        self.num_shares_sold = randint(1800, 2200)
        self.num_shares_bought = randint(1800, 2200)
        return self.current_price, self.num_shares_sold, self.num_shares_bought

    def get_initial_price(self):
        return self.initial_price