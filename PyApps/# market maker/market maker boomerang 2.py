import random


class MarketMaker:
    def __init__(self, initial_price_range, initial_spread, initial_inventory):
        self.price_range = initial_price_range
        self.spread = initial_spread
        self.inventory = initial_inventory
        self.rates_table = [['Iteration', 'Price Range', 'Spread', 'Inventory', 'Average Price']]
        
    def update(self, demand):
        # Get random price/quantity parameters
        price_range = [max(1, self.price_range[0] + random.randint(-5, 5)), min(100, self.price_range[1] + random.randint(-5, 5))]
        spread = max(0.01, min(0.1, self.spread + random.uniform(-0.01, 0.01)))
        inventory = max(0, min(110, self.inventory + random.randint(-20, 20)))
        # Run the market maker algorithm
        bid_price, ask_price, buy_quantity, sell_quantity = self.market_maker_algorithm(price_range, spread, inventory, demand)
        # Update market maker parameters
        self.price_range = price_range
        self.spread = spread
        self.inventory = inventory
        # Add rates to table
        avg_price = (bid_price + ask_price) / 2
        self.rates_table.append([len(self.rates_table), price_range, spread, inventory, avg_price])
        # Return market maker quotes
        return bid_price, ask_price, buy_quantity, sell_quantity
    
    def market_maker_algorithm(self, price_range, spread, inventory, demand):
        mid_price = (price_range[0] + price_range[1]) / 2
        bid_price = mid_price - (spread / 2) * mid_price
        ask_price = mid_price + (spread / 2) * mid_price
        buy_quantity = min(inventory + 20, demand)
        sell_quantity = min(inventory - 20, demand)
        return bid_price, ask_price, buy_quantity, sell_quantity


# Initialize market maker
mm = MarketMaker([15, 15], 0.05, 110)

# Print header
print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<20}".format('Demand', 'Bid Price', 'Ask Price', 'Buy Quantity', 'Sell Quantity', 'Rates'))

# Example monitoring loop
for i in range(10):
    # Get random demand from the market
    demand = random.randint(1, 200)
    # Update market maker and get quotes
    bid_price, ask_price, buy_quantity, sell_quantity = mm.update(demand)
    # Output the results in a table
    print("{:<10} {:<15.2f} {:<15.2f} {:<15} {:<15} {:<20.2f}".format(demand, bid_price, ask_price, buy_quantity, sell_quantity, mm.rates_table[-1][-1]))

# Print footer
print("\nFinal Market Maker Parameters:")
print("Price Range: {}".format(mm.price_range))
print("Spread: {:.2f}".format(mm.spread))
print("Inventory: {}".format(mm.inventory))
print("\nRates Table:")
for row in mm.rates_table:
    print("{:<10} {:<20} {:<10} {:<10} {:<20}".format(row[0], str(row[1]), row[2], row[3], row[4]))