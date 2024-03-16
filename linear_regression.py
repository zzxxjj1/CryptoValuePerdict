import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def load_coin(filename):
    coin_df = pd.read_csv(filename)
    return coin_df

btc_df = load_coin('btc_train.csv')
#print(type(btc_df))
