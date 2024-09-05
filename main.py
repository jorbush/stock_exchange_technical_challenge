def stock_exchanger_broadcast():
    current_share_price = 0
    num_shares_sold = 0
    num_shares_bought = 0
    return { current_share_price, num_shares_sold, num_shares_bought }

def eagy_broker_suggestion(share, num_shares_sold, num_shares_bought, initial_share_price, current_share_price):
    overall_number = num_shares_sold + num_shares_bought
    if num_shares_sold > 2000 and current_share_price <= (initial_share_price - (initial_share_price * (10/100))):
        # Eagy Broker suggests to buy
        raise NotImplementedError
    elif  num_shares_bought > 2000 and current_share_price >= (initial_share_price + (initial_share_price * (10/100))):
        # Eagy Broker suggests to sell
        raise NotImplementedError

if __name__ == '__main__':
    raise NotImplementedError
