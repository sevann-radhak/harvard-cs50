import unittest
from datetime import date, datetime
from seasons import calcule_minutes, format_response, parse_date_birth

class TestSeasons(unittest.TestCase):
    def test_calcule_minutes(self):
        date_birth = date(1991, 5, 27)
        today = date(2022, 1, 1)
        result = calcule_minutes(date_birth, today)
        self.assertEqual(result, 16094880)
        
    def test_calcule_minutes(self):
        date_birth = date(2001, 3, 23)
        today = date(2024, 2, 28)
        result = calcule_minutes(date_birth, today)
        self.assertEqual(result, 12062880)

    def test_format_response(self):
        minutes = 16156800
        result = format_response(minutes)
        self.assertEqual(result, "sixteen million, one hundred fifty-six thousand, eight hundred")

    def test_format_response(self):
        minutes = 12062880
        result = format_response(minutes)
        self.assertEqual(result, "twelve million, sixty-two thousand, eight hundred eighty")

    def test_parse_date_birth(self):
        date_birth = "1991-05-27"
        result = parse_date_birth(date_birth)
        self.assertEqual(result, date(1991, 5, 27))

    def test_parse_date_birth_invalid(self):
        with self.assertRaises(SystemExit):
            parse_date_birth("invalid date")
            
    def test_parse_date_birth_invalid(self):
        with self.assertRaises(SystemExit):
            parse_date_birth("February 6th, 1998")
        
if __name__ == "__main__":
    unittest.main()