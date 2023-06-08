import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

# Load historical BTC price data
btc_data = pd.read_csv("C:/Users/bdefe/Desktop/trading bots/Trading-Bot-AI-ChatGPT/btc_data_2015.csv")  # Replace 'btc_price_data.csv' with the actual file name

# Check the column names in the btc_data DataFrame
print(btc_data.columns)

# Assuming the column containing BTC prices is named 'Price'
btc_prices = btc_data['Price'].values

# Preprocess the data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(btc_prices.reshape(-1, 1))

# Split the data into train and test sets
train_data, test_data = train_test_split(scaled_data, test_size=0.2, shuffle=False)

# Rest of the code remains the same...
