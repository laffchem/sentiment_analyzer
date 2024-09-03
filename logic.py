import yfinance as yf
import numpy as np
import scipy.stats as stats
from datetime import datetime


def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data["Return"] = data["Adj Close"].pct_change()
    data["Return"] = data["Return"] * 100  # Convert to percentages
    return (
        data.dropna()
    )  # Return the entire DataFrame to access both returns and prices


def normalize_and_simulate(data):
    returns = data["Return"]
    mu, std = stats.norm.fit(returns)
    num_sims = 100000
    trading_days = 252
    simulated_returns = np.random.normal(mu, std, (trading_days, num_sims))
    last_price = data["Adj Close"].iloc[-1]

    # Projected price paths
    price_paths = np.zeros_like(simulated_returns)
    price_paths[0] = last_price  # Initialize the first row with the last known price
    for t in range(1, trading_days):
        price_paths[t] = price_paths[t - 1] * (1 + simulated_returns[t] / 100)

    mean_final_price = np.mean(price_paths[-1])
    return mean_final_price


def calculate_percent_change(current_price, projected_price):
    return ((projected_price - current_price) / current_price) * 100


def process_stock(stock_name, ticker, start_date, end_date):
    data = download_data(ticker, start_date, end_date)
    normalized_price = normalize_and_simulate(data)

    # Get the current price
    current_data = yf.download(ticker, period="1d")
    current_price = current_data["Adj Close"].iloc[-1]

    # Calculate percent change
    percent_change = calculate_percent_change(current_price, normalized_price)

    # Print results
    print(f"{stock_name}'s projected mean price in one year: ${normalized_price:.2f}")
    print(f"{stock_name}'s current price: ${current_price:.2f}")
    print(
        f"{stock_name}'s projected percent change from current price to the projected price: {percent_change:.2f}%\n"
    )


def create_exponent():
    today = datetime.now()
    beginning_of_year = datetime(today.year, 1, 1)
    days_from_start = (today - beginning_of_year).days
    exponent = 365 / days_from_start
    return exponent


def calculate_expected_return(initial_investment, ytd, exponent):
    estimated_return = (1 + ytd) ** exponent
    money = initial_investment * estimated_return
    return money


def process_expenses(initial_investment, ytd, stock_name):
    create_exponent()
    money_return = calculate_expected_return(initial_investment, ytd, create_exponent())
    money_return = round(money_return - initial_investment, 2)
    print(f"{stock_name}'s expected return is ${money_return}")
    return money_return
