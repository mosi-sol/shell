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
        if random.random() < 0.5:
            direction = 'buy'
            limit_price = buy_limit
        else:
            direction = 'sell'
            limit_price = sell_limit

        # Check if the limit price is within the price range
        limit_price = max(limit_price, buy_limit)
        limit_price = min(limit_price, sell_limit)

        # Calculate the trade amount
        amount = self.trade_size * limit_price

        # Execute the trade
        if direction == 'buy':
            if self.balance['ETH'] >= amount:
                # Check if the item limit is reached
                if self.inventory_items >= self.item_limit:
                    return
                # Check if the margin is met
                min_eth_balance = self.balance['NFT'] * (100 - self.margin) / 100 * 0.15
                if self.balance['ETH'] - amount < min_eth_balance:
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
                self.total_cost += amount
                print(f'BUY {self.trade_size} {self.symbol} at {limit_price:.2f} ETH ({self.balance})')
        else:
            if self.balance['NFT'] >= self.trade_size:
                # Check if the item limit is reached
                if self.inventory_items <= 0:
                    return
                # Check if the margin is met
                min_eth_balance = self.balance['NFT'] * 0.15
                if self.balance['ETH'] + self.trade_size * limit_price * (100 - self.margin) / 100 > min_eth_balance:
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
                self.total_profit += amount
                print(f'SELL {self.trade_size} {self.symbol} at {limit_price:.2f} ETH ({self.balance})')

    def run(self):
        # Run the market maker algorithm in a loop
        for i in range(self.max_trades):
            self.market_maker()
            time.sleep(1)

        # Return the inventory and other metrics
        return {
            'inventory': self.inventory,
            'total_cost': self.total_cost,
            'total_profit': self.total_profit,
            'balance':self.balance,
            'executed_trades': self.executed_trades
        }

class MarketMakerFactory:
    def create_market_maker(self, nft_balance, eth_balance, symbol='NFT/ETH', spread=0.01, price_range=0.05, trade_size=1, margin=80, item_limit=4200, max_trades=30):
        return MarketMaker(nft_balance, eth_balance, symbol, spread, price_range, trade_size, margin, item_limit, max_trades)

# Example usage
if __name__ == '__main__':
    factory = MarketMakerFactory()
    market_maker = factory.create_market_maker(nft_balance=100, eth_balance=10)
    results = market_maker.run()
    print(f'Inventory: {results["inventory"]}')
    print(f'Total cost: {results["total_cost"]:.2f} ETH')
    print(f'Total profit: {results["total_profit"]:.2f} ETH')
    print(f'Balance: {results["balance"]}')
    print(f'Executed trades: {results["executed_trades"]}')