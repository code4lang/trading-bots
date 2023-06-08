import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load BTC price data from a CSV file or any other source
btc_data = pd.read_csv("C:/Users/bdefe/Desktop/trading bots/Trading-Bot-AI-ChatGPT/btc_data_2015.csv")  # Replace 'btc_data_2015.csv' with the actual file name
# Preprocess the BTC price data
x_train = pd.to_datetime(btc_data['Date'] ).astype('int64')/ 10**5 # Replace 'Date' with the actual column name containing the dates
y_train = pd.to_numeric(btc_data['Price(USD)'])  # Replace 'Price' with the actual column name containing the BTC prices

# Normalize the BTC prices between 0 and 1
y_train = (y_train - y_train.min()) / (y_train.max() - y_train.min())

# Create a sequential model with three layers: a flat input layer, a dense hidden layer with 128 neurons and ReLU activation, and a dense output layer with a single neuron
model = keras.Sequential([
  keras.layers.Flatten(input_shape=(1,)),
  keras.layers.Dense(128, activation='relu'),
  keras.layers.Dense(1)
])

# Compile the model with an appropriate optimizer, loss function, and metrics
model.compile(optimizer='adam',
              loss='mean_squared_error')

print(y_train)
# Train the model using the BTC price data for a certain number of epochs
model.fit(x_train, y_train, epochs=10)

# Predict BTC prices using the trained model
predictions = model.predict(x_train)

# Visualize the predicted BTC prices
plt.plot(x_train, y_train, label='Actual')
plt.plot(x_train, predictions, label='Predicted')
plt.xlabel('Date')
plt.ylabel('BTC Price')
plt.legend()
plt.show()
