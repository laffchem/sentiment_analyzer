import yfinance as yf
import numpy as np
import scipy.stats as stats


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
    num_sims = 10000
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
