class Date:
    date_str = ""

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def convert_date(cls, date_str):
        day, month, year = date_str.split("-")
        return int(day), int(month), int(year)

    @staticmethod
    def validate_date(date):
        day, month, year = date
        return day > 0 and day < 32 and month > 0 and month < 13 and year > 0 and year < 10000


date1 = Date.convert_date("20-11-1996")
print(f"Дата {date1}{' не ' if not Date.validate_date(date1) else ' '}является корректной")

date2 = Date.convert_date("32-05-2000")
print(f"Дата {date2}{' не ' if not Date.validate_date(date2) else ' '}является корректной")
