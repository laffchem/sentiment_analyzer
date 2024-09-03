from utils import start_date, end_date
from logic import process_stock, process_expenses
from config import portfolio, initial_investment, year_to_dates

# Run simulations - obviously could do as loop, just lazy
process_stock("Amazon", portfolio["amazon"], start_date=start_date, end_date=end_date)
process_stock("Apple", portfolio["apple"], start_date=start_date, end_date=end_date)
process_stock("Visa", portfolio["visa"], start_date=start_date, end_date=end_date)
process_stock(
    "Caterpillar", portfolio["caterpillar"], start_date=start_date, end_date=end_date
)
process_stock(
    "United Healthcare",
    portfolio["united_health"],
    start_date=start_date,
    end_date=end_date,
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
