from utils import start_date, end_date
from logic import process_stock, process_expenses
from config import portfolio, initial_investment, year_to_dates

# Run simulations - obviously could do as loop, just lazy
amazon_return = process_stock(
    "Amazon", portfolio["amazon"], start_date=start_date, end_date=end_date
)
apple_return = process_stock(
    "Apple", portfolio["apple"], start_date=start_date, end_date=end_date
)
visa_return = process_stock(
    "Visa", portfolio["visa"], start_date=start_date, end_date=end_date
)
cat_return = process_stock(
    "Caterpillar", portfolio["caterpillar"], start_date=start_date, end_date=end_date
)
united_return = process_stock(
    "United Healthcare",
    portfolio["united_health"],
    start_date=start_date,
    end_date=end_date,
)

monte_carlo_return = round(sum([amazon_return, apple_return, visa_return, cat_return, united_return]) - 1000000, 2)  # type: ignore
print(
    f"The expected return over a year using monte carlo method is ${monte_carlo_return}"
)
# Calculate expected returns - could do as loop, just lazy.
amazon_value = process_expenses(initial_investment, year_to_dates["amazon"], "Amazon")
apple_value = process_expenses(initial_investment, year_to_dates["apple"], "Apple")
visa_value = process_expenses(initial_investment, year_to_dates["visa"], "Visa")
caterpillar_value = process_expenses(
    initial_investment, year_to_dates["caterpillar"], "Caterpillar"
)
united_value = process_expenses(
    initial_investment, year_to_dates["united_health"], "United Healthcare"
)

total = amazon_value + apple_value + visa_value + caterpillar_value + united_value
total = round(total, 2)
print(f"The total amount to return should be approximately ${total}")
