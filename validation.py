from datetime import datetime
from testData import testData

class DateValidation:
    def __init__(self, date):
        self.date = date

    def validate_date(self):
        try: 
            dt = datetime.strptime(self.date, '%Y-%b-%d')
            self.initialize_date()
            return True
        except ValueError:
            raise ValueError("incorrect date format")

    def initialize_date(self):
        if self.date not in testData:
            testData[self.date] = {}
            testData[self.date]["tasks"] = []
