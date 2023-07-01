import time
import random

# Define the trading parameters
symbol = 'BTC/USDT'
spread = 10
price_range = 100
trade_size = 0.01
margin = 80
item_limit = 100
max_trades = 30

# Define the virtual account balance
balance = {
    'BTC': 1,
    'USDT': 5000,
}

# Define the executed trades list
executed_trades = []

# Define the algorithm function
def market_maker():
    # Get the current bid and ask prices
    bid_price = random.uniform(30000, 31000)
    ask_price = random.uniform(31000, 32000)

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
        if balance['USDT'] >= amount:
            # Check if the item limit is reached
            if balance['BTC'] + amount / limit_price > item_limit:
                return
            # Check if the margin is met
            if balance['USDT'] - amount < balance['BTC'] * limit_price * (100 - margin) / 100:
                return
            # Execute the buy order
            balance['BTC'] += amount / limit_price
            balance['USDT'] -= amount
            trade = {
                'direction': direction,
                'amount': amount,
                'price': limit_price
            }
            executed_trades.append(trade)
            print(f'BUY {amount:.2f} {symbol} at {limit_price:.2f} ({balance})')
    else:
        if balance['BTC'] >= trade_size:
            # Check if the item limit is reached
            if balance['BTC'] - trade_size < 0:
                return
            # Check if the margin is met
            if balance['USDT'] + trade_size * limit_price * (100 - margin) / 100 > balance['BTC'] * limit_price:
                return
            # Execute the sell order
            balance['BTC'] -= trade_size
            balance['USDT'] += trade_size * limit_price
            trade = {
                'direction': direction,
                'amount': trade_size,
                'price': limit_price
            }
            executed_trades.append(trade)
            print(f'SELL {trade_size:.2f} {symbol} at {limit_price:.2f} ({balance})')


# Run the market maker algorithm in a loop
for i in range(max_trades):
    market_maker()
    time.sleep(1)

# Show the table of all executed trades
print('\nExecuted Trades:')
print('{:<10} {:<10} {:<10}'.format('Direction', 'Amount', 'Price'))
for trade in executed_trades:
    print('{:<10} {:<10.2f} {:<10.2f}'.format(trade['direction'], trade['amount'], trade['price']))