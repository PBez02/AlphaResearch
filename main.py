from data.fetcher import fetch_prices
from signals.momentum import compute_momentum, momentum_signal

prices = fetch_prices("2020-01-01", "2024-01-01")
momentum = compute_momentum(prices)
signal = momentum_signal(prices)

print(signal.tail())



