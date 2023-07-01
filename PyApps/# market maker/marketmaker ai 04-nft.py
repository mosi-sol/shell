import random
import time

class MarketMaker:
    def __init__(self):
        # Define the trading parameters
        self.symbol = 'NFT/ETH'
        self.spread = 0.01
        self.price_range = 0.05
        self.trade_size = 1
        self.margin = 80
        self.item_limit = 4200
        self.max_trades = 30

        # Define the virtual account balance
        self.balance = {
            'NFT': 100,
            'ETH': 10,
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

        # Show the table of all executed trades
        print('\nExecuted Trades:')
        print('{:<10} {:<10} {:<10} {:<10}'.format('Direction', 'Amount', 'Price (ETH)', 'Total Cost (ETH)'))
        total_cost = 0
        for trade in self.executed_trades:
            cost = trade['amount'] * trade['price']
            total_cost += cost
            print('{:<10} {:<10.2f} {:<10.2f} {:<10.2f}'.format(trade['direction'], trade['amount'], trade['price'], cost))

        # Show the virtual account balance and inventory
        print('\nVirtual Account Balance:')
        print('{:<10} {:<10}'.format('Asset', 'Amount'))
        for asset, amount in self.balance.items():
            print('{:<10} {:<10.4f}'.format(asset, amount))
        print('\nInventory:')
        print('{:<10} {:<10} {:<10}'.format('Type', 'Amount', 'Price (ETH)'))
        for item in self.inventory:
            print('{:<10} {:<10.2f} {:<10.2f}'.format(item['type'], item['amount'], item['price']))
        print(f'\nRemaining Inventory Items: {self.inventory_items}')
        
# =====================================
mm = MarketMaker()
mm.run()