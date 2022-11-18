import unittest
from datetime import datetime

symbol = "IBM"
chart = "2"
time_series = "3"
date_format = "%Y-%m-%d"
start_date = "2022-01-03"
end_date = "2022-01-15"

class symbolTest(unittest.TestCase):
    def test_capitalized(self):
        self.assertTrue(symbol.isupper())

    def test_length(self):
        self.assertTrue(len(symbol) >= 1 and len(symbol) <= 7)

    def test_isalpha(self):
        self.assertTrue(symbol.isalpha())

class chartTest(unittest.TestCase):
    def test_isnum(self):
        self.assertTrue(chart.isnumeric())

    def test_1or2(self):
        self.assertTrue(chart == "1" or chart == "2")

class time_series_Test(unittest.TestCase):
    def test_isnum(self):
        self.assertTrue(time_series.isnumeric() and len(time_series) == 1)

    def test_1through4(self):
        self.assertTrue(time_series == "1" or time_series == "2" or time_series == "3" or time_series == "4")

class start_date_Test(unittest.TestCase):
    def test_dateType(self):
        self.assertTrue(datetime.strptime(start_date, date_format))

class end_date_Test(unittest.TestCase):
    def test_dateType(self):
        self.assertTrue(datetime.strptime(end_date, date_format))


if __name__ == "__main__":
    unittest.main()