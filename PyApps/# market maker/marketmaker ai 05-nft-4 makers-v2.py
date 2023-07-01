import random
import time

class MarketMaker:
    def __init__(self, nft_balance, eth_balance):
        # Define the trading parameters
        self.symbol = 'NFT/ETH'
        self.spread = 0.01
        self.price_range = 0.05
        self.trade_size = 1
        self.margin = 80
        self.item_limit = 4200
        self.max_trades = 5

        # Define the virtual account balance
        self.balance = {
            'NFT': nft_balance,
            'ETH': eth_balance,
        }

        # Define the executed trades list
        self.executed_trades = []

        # Define the inventory list
        self.inventory = []

        # Define the number of inventory items
        self.inventory_items = 100

    def market_maker(self):
        # Get the current bid and ask prices
        bid_price = random.uniform(0.1, 0.2)
        ask_price = random.uniform(0.15, 0.25)

        # Calculate the buy and sell prices
        buy_price = bid_price - self.spread
        sell_price = ask_price + self.spread

        # Set the price range limit
        price_limit = self.price_range / 2

        # Determine the buy and sell limits
        buy_limit = buy_price - price_limit
        sell_limit = sell_price + price_limit

        # Determine the trade direction
        if random.random() < 0.5:
            direction = 'buy'
            limit_price = buy_limit
        else:
            direction = 'sell'
            limit_price = sell_limit

        # Check if the limit price is within the price range
        if limit_price < buy_limit:
            limit_price = buy_limit
        elif limit_price > sell_limit:
            limit_price = sell_limit

        # Calculate the trade amount
        amount = self.trade_size * limit_price

        # Execute the trade
        if direction == 'buy':
            if self.balance['ETH'] >= amount:
                # Check if the item limit is reached
                if self.inventory_items >= self.item_limit:
                    return
                # Check if the margin is met
                if self.balance['ETH'] - amount < self.balance['NFT'] * (100 - self.margin) / 100 * 0.15:
                    return
                # Execute the buy order
                self.balance['NFT'] += self.trade_size
                self.balance['ETH'] -= amount
                self.inventory.append({
                    'amount': self.trade_size,
                    'price': limit_price,
                    'type': 'buy'
                })
                trade = {
                    'direction': direction,
                    'amount': self.trade_size,
                    'price': limit_price
                }
                self.executed_trades.append(trade)
                self.inventory_items += 1
                print(f'BUY {self.trade_size} {self.symbol} at {limit_price:.2f} ETH ({self.balance})')
        else:
            if self.balance['NFT'] >= self.trade_size:
                # Check if the item limit is reached
                if self.inventory_items <= 0:
                    return
                # Check if the margin is met
                if self.balance['ETH'] + self.trade_size * limit_price * (100 - self.margin) / 100 > self.balance['NFT'] * 0.15:
                    return
                # Execute the sell order
                self.balance['NFT'] -= self.trade_size
                self.balance['ETH'] += amount
                self.inventory.append({
                    'amount': self.trade_size,
                    'price': limit_price,
                    'type': 'sell'
                })
                trade = {
                    'direction': direction,
                    'amount': self.trade_size,
                    'price': limit_price
                }
                self.executed_trades.append(trade)
                self.inventory_items -= 1
                print(f'SELL {self.trade_size} {self.symbol} at {limit_price:.2f} ETH ({self.balance})')

    def run(self):
        # Run the market maker algorithm in a loop
        for i in range(self.max_trades):
            self.market_maker()
            time.sleep(1)

        # Return the list of all executed trades
        return self.executed_trades
        
        
# ===============================

def combine_executed_trades(executed_trades_list):
    # Combine the executed trades for all market makers into a single list
    all_executed_trades = []
    for executed_trades in executed_trades_list:
        all_executed_trades.extend(executed_trades)

    # Sort the trades by price
    sorted_trades = sorted(all_executed_trades, key=lambda x: x['price'])

    # Print the trades in a table
    print('Market Maker\tDirection\tAmount\tPrice')
    print('--------------------------------------------------')
    for trade in sorted_trades:
        market_maker = executed_trades_list.index([d for d in executed_trades_list if trade in d][0]) + 1
        print(f'Market Maker {market_maker}\t{trade["direction"].capitalize()}\t\t{trade["amount"]}\t{trade["price"]}')

# ===============================

# Create four instances of the MarketMaker class with different account balances
mm1 = MarketMaker(100, 10)
mm2 = MarketMaker(50, 20)
mm3 = MarketMaker(200, 5)
mm4 = MarketMaker(150, 15)

# Run the market maker algorithm on each instance
executed_trades1 = mm1.run()
executed_trades2 = mm2.run()
executed_trades3 = mm3.run()
executed_trades4 = mm4.run()

# Combine the executed trades for all market makers into a single table
combine_executed_trades([executed_trades1, executed_trades2, executed_trades3, executed_trades4])

# ===============================