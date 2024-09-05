from stock_exchanger import StockExchanger
from eagy_broker import EagyBroker

if __name__ == '__main__':
    share = "AMZN"
    exchanger = StockExchanger(share)
    broker = EagyBroker()
    # simulate 10 exchanges
    for _ in range(10):
        current_price, num_shares_sold, num_shares_bought = exchanger.broadcast()
        print(broker.suggest(share, num_shares_sold, num_shares_bought, exchanger.get_initial_price(), current_price))
