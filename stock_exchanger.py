from random import randint
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
                self.current_price = randint(60, 140)
                self.queue.put((self.share, 'price', self.current_price))
            time.sleep(60)

    def broadcast_volume(self):
        """Broadcasts the number of shares sold or bought every second"""
        while True:
            with self.lock:
                self.num_shares_sold = randint(1800, 2200)
                self.num_shares_bought = randint(1800, 2200)
                self.queue.put(
                    (self.share, 'volume', self.num_shares_sold, self.num_shares_bought))
            time.sleep(1)
