import streamlit as st
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Function to get stock data from yfinance API
def get_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Function to preprocess data and create features
def preprocess_data(data):
    data['Date'] = data.index
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    data['Day'] = data['Date'].dt.day
    return data

# Function to train machine learning model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Function to evaluate model
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

# Main function
def main():
    st.title('Stock Price Prediction')

    # Input form for user
    symbol = st.text_input('Enter stock symbol (e.g., AAPL for Apple Inc.):', 'AAPL')
    start_date = st.date_input('Enter start date:')
    end_date = st.date_input('Enter end date:')

    # Fetching stock data
    if start_date < end_date:
        data = get_stock_data(symbol, start_date, end_date)
        st.write('Stock Data:')
        st.write(data.head())
    else:
        st.error('End date must be after start date.')

    # Preprocessing data
    if 'Close' in data.columns:
        data = preprocess_data(data)
        X = data[['Year', 'Month', 'Day']]
        y = data['Close']

        # Training model
        model, X_test, y_test = train_model(X, y)
        st.write('Model trained successfully!')

        # Evaluating model
        mse = evaluate_model(model, X_test, y_test)
        st.write(f'Mean Squared Error: {mse}')

        # Predicting stock price for tomorrow
        tomorrow_date = end_date + pd.DateOffset(days=1)
        tomorrow_data = pd.DataFrame({'Year': tomorrow_date.year,
                                      'Month': tomorrow_date.month,
                                      'Day': tomorrow_date.day}, index=[0])
        prediction = model.predict(tomorrow_data)[0]

        st.write(f'Predicted stock price for tomorrow: {prediction}')

        # Decision to buy or sell
        current_price = data['Close'].iloc[-1]
        if prediction > current_price:
            st.write('Recommendation: Stock is buyable.')
        elif prediction < current_price:
            st.write('Recommendation: Stock is sellable.')
        else:
            st.write('Recommendation: Hold position.')
    else:
        st.error('Close price data not found in the provided date range.')

if __name__ == '__main__':
    main()