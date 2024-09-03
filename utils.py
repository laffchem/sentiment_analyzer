from datetime import datetime, timedelta

end_date = datetime.today()
start_date = end_date - timedelta(
    365
    * int(
        input(
            "Enter the amount of years you would like to analyze over. (1, 2, 3, etc...)\n"
        )
    )
)

end_date_str = end_date.strftime("%Y-%m-%d")
start_date_str = start_date.strftime("%Y-%m-%d")
