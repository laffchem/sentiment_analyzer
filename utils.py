from datetime import datetime, timedelta

years = int(
    input("Enter the number of years you would like to analyze. (1, 2, 3, etc...)\n")
)
end_date = datetime.today()
start_date = end_date - timedelta(365 * years)

end_date_str = end_date.strftime("%Y-%m-%d")
start_date_str = start_date.strftime("%Y-%m-%d")
