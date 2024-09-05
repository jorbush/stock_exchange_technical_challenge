from random import randint

def stock_exchanger_broadcast():
    current_share_price = randint(60, 140)
    num_shares_sold = randint(1800, 2200)
    num_shares_bought = randint(1800, 2200)
    return current_share_price, num_shares_sold, num_shares_bought

def eagy_broker_suggestion(share, num_shares_sold, num_shares_bought, initial_share_price, current_share_price):
    print(f"num_shares_sold: {num_shares_sold} num_shares_bought: {num_shares_bought} initial_share_price: {initial_share_price} current_share_price: {current_share_price}")
    if num_shares_sold > 2000 and current_share_price <= (initial_share_price * 0.9):
        return f"Eagy Broker suggests to BUY {share}"
    elif  num_shares_bought > 2000 and current_share_price >= (initial_share_price * 1.1):
        return f"Eagy Broker suggests to SELL {share}"
    return f"Eagy Broker suggests to HOLD {share}"

if __name__ == '__main__':
    share = "AMZN"
    initial_share_price = 100
    print(f"Initial share price for {share}: {initial_share_price}")
    # simulate 10 stock exchanges
    for i in range(10):
        current_share_price, num_shares_sold, num_shares_bought = stock_exchanger_broadcast()
        suggestion = eagy_broker_suggestion(share, num_shares_sold, num_shares_bought, initial_share_price, current_share_price)
        print(suggestion)
