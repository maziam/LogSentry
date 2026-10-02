import unittest
from logsentry.detector import count_failed_logins, detect_suspicious_ips

class TestDetector(unittest.TestCase):
    def test_detection(self):
        records=[{"event":"Failed","ip":"1.1.1.1","username":"root"}]*3
        counts=count_failed_logins(records)
        self.assertIn("1.1.1.1", detect_suspicious_ips(counts,3))

if __name__ == "__main__":
    unittest.main()
