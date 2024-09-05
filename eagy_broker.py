class EagyBroker:
    def suggest(self, share, num_shares_sold, num_shares_bought, initial_price, current_price):
        print(f"\nnum_shares_sold: {num_shares_sold} num_shares_bought: {num_shares_bought} initial_price: {initial_price} current_price: {current_price}")
        if num_shares_sold > 2000 and current_price <= initial_price * 0.9:
            return f"Eagy Broker suggests to BUY {share}"
        elif num_shares_bought > 2000 and current_price >= initial_price * 1.1:
            return f"Eagy Broker suggests to SELL {share}"
        return f"Eagy Broker suggests to HOLD {share}"
