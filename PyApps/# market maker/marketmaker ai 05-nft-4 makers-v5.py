import random
import time

class MarketMaker:
    def __init__(self, nft_balance, eth_balance, symbol='NFT/ETH', spread=0.01, price_range=0.05, trade_size=1, margin=80, item_limit=4200, max_trades=30):
        # Define the trading parameters
        self.symbol = symbol
        self.spread = spread
        self.price_range = price_range
        self.trade_size = trade_size
        self.margin = margin
        self.item_limit = item_limit
        self.max_trades = max_trades

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
        self.inventory_items = 0

        # Define the total cost and total profit
        self.total_cost = 0
        self.total_profit = 0

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
        direction = 'buy' if random.random() < 0.5 else 'sell'
        limit_price = buy_limit if direction == 'buy' else sell_limit

        # Check if the limit price is within the price range
        limit_price = max(limit_price, buy_limit)
        limit_price = min(limit_price, sell_limit)

        # Calculate the trade amount
        amount = self.trade_size * limit_price

        # Execute the trade
        if direction == 'buy':
            if self.balance['ETH'] >= amount and self.inventory_items < self.item_limit and self.balance['ETH'] - amount >= self.balance['NFT'] * (100 - self.margin) / 100 * 0.15:
                self.balance['NFT'] += self.trade_size
                self.balance['ETH'] -= amount
                self.inventory.append({'amount': self.trade_size, 'price': limit_price, 'type': 'buy'})
                trade = {'direction': direction, 'amount': self.trade_size, 'price': limit_price}
                self.executed_trades.append(trade)
                self.inventory_items += 1
                self.total_cost += amount
                print(f'BUY {self.trade_size} {self.symbol} at {limit_price:.2f} ETH ({self.balance})')
        else:
            if self.balance['NFT'] >= self.trade_size and self.inventory_items > 0 and self.balance['ETH'] + self.trade_size * limit_price * (100 - self.margin) / 100 <= self.balance['NFT'] * 0.15:
                self.balance['NFT'] -= self.trade_size
                self.balance['ETH'] += amount
                self.inventory.append({'amount': self.trade_size, 'price': limit_price, 'type': 'sell'})
                trade = {'direction': direction, 'amount': self.trade_size, 'price': limit_price}
                self.executed_trades.append(trade)
                self.inventory_items -= 1
                self.total_profit += amount
                print(f'SELL {self.trade_size} {self.symbol} at {limit_price:.2f} ETH ({self.balance})')

    def run(self):
        # Run the market maker algorithm in a loop
        for i in range(self.max_trades):
            self.market_maker()
            time.sleep(1)

        # Format the inventory and executed trades output as plain strings
        inventory_str = 'Amount\tPrice\tType\n'
        for item in self.inventory:
            inventory_str += f'{item["amount"]}\t{item["price"]:.2f}\t{item["type"].upper()}\n'
        trades_str = 'Direction\tAmount\tPrice\n'
        for trade in self.executed_trades:
            trades_str += f'{trade["direction"].upper()}\t{trade["amount"]}\t{trade["price"]:.2f}\n'

        # Print the inventory and executed trades output
        print('Inventory:\n' + inventory_str)
        print('Executed trades:\n' + trades_str)
        
# ===================================
# Create a market maker with 100 NFT and 10 ETH balances
market_maker = MarketMaker(100, 10)

# Run the market maker algorithm for 30 trades
market_maker.run()