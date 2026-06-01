import pandas as pd
import numpy as np

def compute_mr(prices: pd.DataFrame,
               window: int = 60) -> pd.DataFrame:
    mean = prices.rolling(window).mean()
    std = prices.rolling(window).std()
    z = (prices - mean) / std
    signal = np.where(z > 2,-1, np.where(z < -2, 1, 0))
    return pd.DataFrame(signal, index = prices.index, columns=prices.columns)