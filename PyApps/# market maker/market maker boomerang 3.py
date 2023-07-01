import random 

class MarketMaker:
    def __init__(self, initial_price_range, initial_spread, initial_inventory, historical_prices):
        self.price_range = initial_price_range
        self.spread = initial_spread
        self.inventory = initial_inventory
        self.rates_table = [['Iteration', 'Price Range', 'Spread', 'Inventory', 'Average Price']]
        self.historical_prices = historical_prices
        self.growth_rate = 0.01
        self.min_spread = 0.01
        self.max_spread = 0.1
        self.min_inventory = 20
        self.max_inventory = 200
        self.demand_history = []
        self.price_history = []
    
    def update(self, demand):
        # Update demand history
        self.demand_history.append(demand)
        # Get random price/quantity parameters
        price_range = [max(1, self.price_range[0] + random.randint(-5, 5)), min(100, self.price_range[1] + random.randint(-5, 5))]
        spread = max(self.min_spread, min(self.max_spread, self.spread + random.uniform(-0.01, 0.01)))
        inventory = max(self.min_inventory, min(self.max_inventory, self.inventory + random.randint(-20, 20)))
        # Run the market maker algorithm with growth adjustment
        mid_price = (self.price_range[0] + self.price_range[1]) / 2
        mid_price *= (1 + self.growth_rate)
        bid_price, ask_price, buy_quantity, sell_quantity = self.market_maker_algorithm(mid_price, price_range, spread, inventory, demand)
        # Update market maker parameters
        self.price_range = price_range
        self.spread = spread
        self.inventory = inventory
        # Add rates to table
        avg_price = (bid_price + ask_price) / 2
        self.rates_table.append([len(self.rates_table), price_range, spread, inventory, avg_price])
        # Update price history
        self.price_history.append(avg_price)
        # Return market maker quotes
        return bid_price, ask_price, buy_quantity, sell_quantity
    
    def calculate_regression(self, x, y):
        n = len(x)
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        numer = sum([xi*yi for xi,yi in zip(x,y)]) - n * x_mean * y_mean
        denom = sum([xi**2 for xi in x]) - n * x_mean**2
        slope = numer / denom
        return slope
    
    def market_maker_algorithm(self, mid_price, price_range, spread, inventory, demand):
        # Calculate regression line for historical prices
        if len(self.price_history) > 10:
            x = self.demand_history[-10:]
            y = self.price_history[-10:]
            price_slope = self.calculate_regression(x, y)
        else:
            price_slope = 0
        # Calculate bid and ask prices
        spread_adjustment = spread * (1 - inventory / self.max_inventory)
        bid_price = mid_price - (spread / 2) * mid_price - spread_adjustment * mid_price
        ask_price = mid_price + (spread / 2) * mid_price + spread_adjustment * mid_price
        # Adjust bid and ask prices based on historical price trend
        if price_slope > 0:
            bid_price *= (1 - min(0.05, price_slope))
            ask_price *= (1 + min(0.05, price_slope))
        elif price_slope < 0:
            bid_price *= (1 + min(0.05, -price_slope))
            ask_price *= (1 - min(0.05, -price_slope))
        # Adjust bid and ask prices based on demand
        if demand > inventory:
            buy_quantity = min(inventory + 20, demand)
            sell_quantity = 0
            ask_price *= (1 + 0.05)
        else:
            buy_quantity = 0
            sell_quantity = min(inventory - 20, demand)
            bid_price *= (1 - 0.05)
        return bid_price, ask_price, buy_quantity, sell_quantity
        
# =============================
# an instance of the MarketMaker class, passing in the initial price range, initial spread, initial inventory, and historical prices (as a list of numbers).
mm = MarketMaker([50, 60], 0.02, 100, [55, 57, 58, 56, 54, 52, 50, 48, 46, 44])

print("===========================")

def run():
    num = random.randint(1, 10)
    bid_price, ask_price, buy_quantity, sell_quantity = mm.update(num)
    print('Bid price:', bid_price)
    print('Ask price:', ask_price)
    print('Buy quantity:', buy_quantity)
    print('Sell quantity:', sell_quantity)
    if (buy_quantity == 0):
        print("profit: +", sell_quantity * ask_price)
    if (sell_quantity == 0):
        print("cost: -", buy_quantity * bid_price)
    print("===========================")


for i in range(4):
    run()

# ------------------------------------

print('Historical rates:')
for row in mm.rates_table:
    print(row)

print('\nPrice history:', mm.price_history)
print("===========================")