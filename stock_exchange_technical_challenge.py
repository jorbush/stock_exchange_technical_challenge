from stock_exchanger import StockExchanger
from eagy_broker import EagyBroker
from queue import Queue
import threading


def stock_exchange_technical_challenge():
    event_queue = Queue()

    amazon_exchanger = StockExchanger('AMZN', event_queue)
    apple_exchanger = StockExchanger('AAPL', event_queue)
    broker = EagyBroker()

    broker.subscribe(amazon_exchanger)
    broker.subscribe(apple_exchanger)

    amazon_price_thread = threading.Thread(
        target=amazon_exchanger.broadcast_price, daemon=True)
    amazon_volume_thread = threading.Thread(
        target=amazon_exchanger.broadcast_volume, daemon=True)
    apple_price_thread = threading.Thread(
        target=apple_exchanger.broadcast_price, daemon=True)
    apple_volume_thread = threading.Thread(
        target=apple_exchanger.broadcast_volume, daemon=True)

    amazon_price_thread.start()
    amazon_volume_thread.start()
    apple_price_thread.start()
    apple_volume_thread.start()

    try:
        while True:
            broker.process_event(event_queue.get())
    except KeyboardInterrupt:
        print(f"\nSimulation stopped.")
        pass


if __name__ == '__main__':
    stock_exchange_technical_challenge()
