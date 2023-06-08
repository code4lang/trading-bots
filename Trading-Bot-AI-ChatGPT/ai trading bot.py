import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load BTC price data from a CSV file
data = pd.read_csv('C:/Users/bdefe\Desktop/btc_data_2015.csv')  # Replace 'btc_price_data.csv' with the actual filename and path of your BTC price data file

# Split the data into training and test sets
train_data = data[data['date'] < '2016']  # Filter data for training period (replace '2016' with the desired training end year)
test_data = data[data['date'] >= '2016']  # Filter data for test period (replace '2016' with the desired test start year)

# Normalize the BTC price values between 0 and 1
max_price = train_data['price'].max()
min_price = train_data['price'].min()
train_data['price'] = (train_data['price'] - min_price) / (max_price - min_price)
test_data['price'] = (test_data['price'] - min_price) / (max_price - min_price)

# Prepare the training and test data
x_train = np.array(train_data['input_feature'])  # Replace 'input_feature' with the actual name of the input feature column in your data
y_train = np.array(train_data['price'])
x_test = np.array(test_data['input_feature'])  # Replace 'input_feature' with the actual name of the input feature column in your data
y_test = np.array(test_data['price'])

# Create a sequential model with appropriate layers for your BTC price prediction
model = keras.Sequential([
  keras.layers.Dense(128, activation='relu', input_shape=(1,)),  # Adjust the input shape as per your input feature dimensions
  keras.layers.Dense(64, activation='relu'),
  keras.layers.Dense(1)  # Output layer with a single neuron for price prediction
])

# Compile the model with an appropriate optimizer and loss function for regression
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model with the training data
model.fit(x_train, y_train, epochs=10, batch_size=32)  # Adjust the number of epochs and batch size as needed

# Evaluate the model using the test data
test_loss = model.evaluate(x_test, y_test)
print('\nTest loss:', test_loss)

# Make predictions using the test data
predictions = model.predict(x_test)

# Visualize the predicted prices and actual prices
plt.plot(test_data['date'], y_test, label='Actual Price')
plt.plot(test_data['date'], predictions, label='Predicted Price')
plt.xlabel('Date')
plt.ylabel('BTC Price')
plt.title('BTC Price Prediction')
plt.legend()
plt.show()
