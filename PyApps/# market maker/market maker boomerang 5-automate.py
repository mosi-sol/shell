import time
import random

# define a function to get the current market price
def get_current_price():
    return random.randint(1, 500)  # example function that returns a random price between 1 and 500

# define a function to place a buy order
def place_buy_order():
    print("Placing a buy order...")  # example function that prints a message

# define a function to place a sell order
def place_sell_order():
    print("Placing a sell order...")  # example function that prints a message

# determine the price range and spread
historical_sales_data = [100, 200, 150, 300, 250]  # example historical sales data
average_sale_price = sum(historical_sales_data) / len(historical_sales_data)
spread = 0.1  # example spread
bid_price = average_sale_price * (1 - spread)
ask_price = average_sale_price * (1 + spread)

# set the inventory level
inventory_level = 100  # example inventory level

# create an empty list to store the simulation results
simulation_results = []

# loop for a certain number of iterations to simulate the market
for i in range(30):
    # get the current market price
    current_price = get_current_price()

    # initialize the action variable to None
    action = None

    # if the current price is lower than the bid price and there are NFTs in inventory, place a buy order
    if current_price < bid_price and inventory_level > 0:
        place_buy_order()
        inventory_level -= 1
        action = "Buy"

    # if the current price is higher than the ask price, place a sell order
    elif current_price > ask_price:
        place_sell_order()
        inventory_level += 1
        action = "Sell"

    # adjust the bid and ask prices based on the current inventory level
    if inventory_level <= 10:
        spread = 0.2  # increase the spread if inventory is low
    elif inventory_level >= 90:
        spread = 0.05  # decrease the spread if inventory is high
    else:
        spread = 0.1  # keep the spread constant

    bid_price = average_sale_price * (1 - spread)
    ask_price = average_sale_price * (1 + spread)

    # add the current simulation step's results to the simulation_results list
    simulation_results.append({'Iteration': i+1, 'Current Price': current_price, 'Bid Price': bid_price, 'Ask Price': ask_price, 'Inventory Level': inventory_level, 'Action': action})

    # wait for a certain amount of time before checking the market again
    time.sleep(1)  # for example, wait for 1 second

# create a table format string
table_format = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}"

# print table header
print(table_format.format("Iteration", "Current Price", "Bid Price", "Ask Price", "Inventory Level", "Action"))

# print table rows
for row in simulation_results:
    print(table_format.format(row['Iteration'], row['Current Price'], row['Bid Price'], row['Ask Price'], row['Inventory Level'], row['Action']))