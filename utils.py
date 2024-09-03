from datetime import datetime, timedelta

end_date = datetime.today()
start_date = end_date - timedelta(365)

end_date_str = end_date.strftime("%Y-%m-%d")
start_date_str = start_date.strftime("%Y-%m-%d")
