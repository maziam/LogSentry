import re

PATTERN = re.compile(
    r"(?P<event>Failed|Accepted) password for (?P<username>\S+) from (?P<ip>\S+)"
)

def parse_log(line):
    m = PATTERN.search(line)
    if not m:
        return None
    return m.groupdict()

def parse_file(filename):
    records=[]
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            r = parse_log(line)
            if r:
                records.append(r)
    return records
