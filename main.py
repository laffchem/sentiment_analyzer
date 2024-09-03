from utils import start_date, end_date
from logic import process_stock
from config import portfolio

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
