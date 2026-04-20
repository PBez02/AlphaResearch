from data.fetcher import fetch_prices

prices = fetch_prices("2020-01-01", "2024-01-01")
print(prices.shape)
print(prices.head())

