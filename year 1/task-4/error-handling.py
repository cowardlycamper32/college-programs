import datetime as dt

def dateCheck(date1: str, date2: str) -> bool:
    parsed_date_1 = dt.datetime.strptime(date1, "%d-%m-%Y")
    parsed_date_2 = dt.datetime.strptime(date2, "%d-%m-%Y")

    if parsed_date_1 > parsed_date_2:
        return False
    else:
        return True


print(str(dateCheck("01-02-2003", "02-03-2004")) + ", " + str(dateCheck("02-03-2004", "01-02-2003")))
