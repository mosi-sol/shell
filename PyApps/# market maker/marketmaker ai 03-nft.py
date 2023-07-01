import time
import random

# Define the trading parameters
symbol = 'NFT/ETH'
spread = 0.01
price_range = 0.05
trade_size = 1
margin = 80
item_limit = 4200
max_trades = 10

# Define the virtual account balance
balance = {
    'NFT': 100,
    'ETH': 10,
}

# Define the executed trades list
executed_trades = []

# Define the inventory list
inventory = []

# Define the algorithm function
def market_maker():
    # Get the current bid and ask prices
    bid_price = random.uniform(0.1, 0.2)
    ask_price = random.uniform(0.15, 0.25)

    # Calculate the buy and sell prices
    buy_price = bid_price - spread
    sell_price = ask_price + spread

    # Set the price range limit
    price_limit = price_range / 2

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
    amount = trade_size * limit_price

    # Execute the trade
    if direction == 'buy':
        if balance['ETH'] >= amount:
            # Check if the item limit is reached
            if balance['NFT'] + trade_size > item_limit:
                return
            # Check if the margin is met
            if balance['ETH'] - amount < balance['NFT'] * (100 - margin) / 100 * 0.15:
                return
            # Execute the buy order
            balance['NFT'] += trade_size
            balance['ETH'] -= amount
            inventory.append({
                'amount': trade_size,
                'price': limit_price,
                'type': 'buy'
            })
            trade = {
                'direction': direction,
                'amount': trade_size,
                'price': limit_price
            }
            executed_trades.append(trade)
            print(f'BUY {trade_size} {symbol} at {limit_price:.2f} ETH ({balance})')
    else:
        if balance['NFT'] >= trade_size:
            # Check if the item limit is reached
            if balance['NFT'] - trade_size < 0:
                return
            # Check if the margin is met
            if balance['ETH'] + trade_size * limit_price * (100 - margin) / 100 > balance['NFT'] * 0.15:
                return
            # Execute the sell order
            balance['NFT'] -= trade_size
            balance['ETH'] += amount
            inventory.append({
                'amount': trade_size,
                'price': limit_price,
                'type': 'sell'
            })
            trade = {
                'direction': direction,
                'amount': trade_size,
                'price': limit_price
            }
            executed_trades.append(trade)
            print(f'SELL {trade_size} {symbol} at {limit_price:.2f} ETH ({balance})')


# Run the market maker algorithm in a loop
for i in range(max_trades):
    market_maker()
    time.sleep(1)

# Show the table of all executed trades
print('\nExecuted Trades:')
print('{:<10} {:<10} {:<10} {:<10}'.format('Direction', 'Amount', 'Price (ETH)', 'Total Cost (ETH)'))
total_cost = 0
for trade in executed_trades:
    cost = trade['amount'] * trade['price']
    total_cost += cost
    print('{:<10} {:<10.2f} {:<10.2f} {:<10.2f}'.format(trade['direction'], trade['amount'], trade['price'], cost))
    
# Show the inventory table
print('\nInventory:')
print('{:<10} {:<10} {:<10} {:<10}'.format('Type', 'Amount', 'Price (ETH)', 'Total Value (ETH)'))
total_value = 0
for item in inventory:
    value = item['amount'] * item['price']
    total_value += value
    print('{:<10} {:<10.2f} {:<10.2f} {:<10.2f}'.format(item['type'], item['amount'], item['price'], value))

# Calculate the total profit and inventory value
total_profit = total_value - total_cost
inventory_items = sum(item['amount'] for item in inventory)
inventory_value = inventory_items * 0.15

# Show the summary table
print('\nSummary:')
print('{:<30} {:<10}'.format('Total Inventory Items:', inventory_items))
print('{:<30} {:<10.2f}'.format('Total Cost (ETH):', total_cost))
print('{:<30} {:<10.2f}'.format('Total Value (ETH):', total_value))
print('{:<30} {:<10.2f}'.format('Total Profit (ETH):', total_profit))
print('{:<30} {:<10.2f}'.format('Inventory Value (ETH):', inventory_value))
print('{:<30} {:<10.2f}'.format('Total Account Balance (ETH):', balance['ETH']))