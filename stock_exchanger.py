from random import randint, random
import threading
import time
from queue import Queue


class StockExchanger:
    def __init__(self, share, queue: Queue):
        self.share = share
        self.initial_price = randint(80, 120)
        self.current_price = self.initial_price
        self.num_shares_sold = 0
        self.num_shares_bought = 0
        self.lock = threading.Lock()
        self.queue = queue

    def broadcast_price(self):
        """Broadcasts the current price of the share every minute"""
        while True:
            with self.lock:
                self.update_price()
                self.queue.put((self.share, 'price', self.current_price))
                self.num_shares_sold, self.num_shares_bought = 0, 0
            time.sleep(60)

    def broadcast_volume(self):
        """Broadcasts the number of shares sold or bought every second"""
        while True:
            with self.lock:
                if random() < 0.5:
                    shares_sold, shares_bought = randint(1, 1000), 0
                    self.num_shares_sold += shares_sold
                else:
                    shares_bought, shares_sold  = randint(1, 1000), 0
                    self.num_shares_bought += shares_bought
                self.queue.put((self.share, 'volume', shares_sold, shares_bought))
            time.sleep(1)

    def update_price(self):
        """Updates the price based on the amount of shares bought or sold."""
        if self.num_shares_bought + self.num_shares_sold == 0: return
        p_increase = self.num_shares_sold / (self.num_shares_bought + self.num_shares_sold)
        if random() < p_increase:
            self.current_price = int(self.current_price * 1.1)
        else:
            self.current_price = int(self.current_price * 0.9)