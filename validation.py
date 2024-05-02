from datetime import datetime
from flask import redirect, url_for

class DateValidation:
    def __init__(self, date):
        self.date = date

    def validate_date(self):
        try: 
            dt = datetime.strptime(self.date, '%Y-%b-%d')
            return {}
        except ValueError: 
            return {
                "error": "invalid date format",
            }
