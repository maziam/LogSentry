import unittest
from logsentry.parser import parse_log

class TestParser(unittest.TestCase):
    def test_parse(self):
        r=parse_log("Failed password for root from 10.0.0.1")
        self.assertEqual(r["ip"],"10.0.0.1")

if __name__ == "__main__":
    unittest.main()
