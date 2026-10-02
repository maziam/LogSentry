import argparse, os
from logsentry.parser import parse_file
from logsentry.detector import count_failed_logins, detect_suspicious_ips
from logsentry.report import print_report

def main():
    p=argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--threshold", type=int, default=3)
    a=p.parse_args()

    if not os.path.isfile(a.file):
        p.error("log file does not exist")
    if a.threshold <= 0:
        p.error("threshold must be greater than 0")

    records=parse_file(a.file)
    counts=count_failed_logins(records)
    suspicious=detect_suspicious_ips(counts,a.threshold)
    print_report(counts,suspicious,a.threshold)
