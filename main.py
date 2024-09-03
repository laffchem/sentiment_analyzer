from utils import start_date, end_date
from logic import download_data, normalize_and_simulate
from config import portfolio

amazon_data = download_data(
    portfolio["amazon"], start_date=start_date, end_date=end_date
)
amazon_normalized = normalize_and_simulate(amazon_data)
print(f"Amazon's projected mean price in one year: ${amazon_normalized:.2f}")

apple_data = download_data(portfolio["apple"], start_date=start_date, end_date=end_date)
apple_normalized = normalize_and_simulate(apple_data)
print(f"Apple's projected mean price in one year: ${apple_normalized:.2f}")

visa_data = download_data(portfolio["visa"], start_date=start_date, end_date=end_date)
visa_normalized = normalize_and_simulate(visa_data)
print(f"Visa's projected mean price in one year: ${visa_normalized:.2f}")

caterpillar_data = download_data(
    portfolio["caterpillar"], start_date=start_date, end_date=end_date
)
caterpillar_normalized = normalize_and_simulate(caterpillar_data)
print(f"Caterpillar's projected mean price in one year: ${caterpillar_normalized:.2f}")

united_health_data = download_data(
    portfolio["united_health"], start_date=start_date, end_date=end_date
)
united_health_normalized = normalize_and_simulate(united_health_data)
print(
    f"United Healthcare's projected mean price in one year: ${united_health_normalized:.2f}"
)
