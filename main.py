from data.fetcher import fetch_prices
from signals.momentum import compute_momentum, momentum_signal
from signals.mean_reversion import compute_mr

prices = fetch_prices("2020-01-01", "2024-01-01")
signal = compute_mr(prices)

print(signal.tail())



