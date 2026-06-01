import pandas as pd
import numpy as np

def compute_momentum(prices: pd.DataFrame,
                      long_window: int = 252,
                      skip: int = 21) -> pd.DataFrame:
    return prices.shift(skip) / prices.shift(long_window) - 1

def momentum_signal(prices: pd.DataFrame) -> pd.DataFrame:
    raw = compute_momentum(prices)
    return np.sign(raw)