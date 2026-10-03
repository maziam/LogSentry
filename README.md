# LogSentry

LogSentry is a lightweight Python command-line tool for analyzing authentication logs and detecting repeated failed login attempts.

## Features

- Parse authentication logs
- Detect failed login attempts
- Count failed logins by IP address
- Configurable detection threshold
- Identify suspicious IP addresses
- Simple modular architecture
- Unit tests
- No external Python dependencies

## Requirements

- Python 3.10+

LogSentry uses only the Python standard library.

## Usage

Analyze a log file with the default threshold:

```bash
python3 main.py auth.log
```

Use a custom threshold:

```bash
python3 main.py auth.log --threshold 3
```

## Example Log

```text
Failed password for root from 192.168.1.20
Failed password for admin from 192.168.1.20
Accepted password for mazdak from 192.168.1.5
Failed password for root from 192.168.1.20
Failed password for root from 10.0.0.7
Failed password for test from 192.168.1.20
Failed password for root from 192.168.1.20
```

## Example Output

```text
Threshold: 3

Failed Login Counts:
192.168.1.20 -> 5
10.0.0.7 -> 1

Suspicious IPs:
192.168.1.20 -> SUSPICIOUS -> 5
```

## Architecture

```text
Log File
   ↓
Parser
   ↓
Structured Records
   ↓
Detector
   ↓
Report
```

## Module Responsibilities

- `main.py` — application entry point
- `logsentry/cli.py` — command-line interface and orchestration
- `logsentry/parser.py` — parses raw authentication log lines
- `logsentry/detector.py` — counts failed logins and detects suspicious IP addresses
- `logsentry/report.py` — formats and displays terminal output

## Project Structure

```text
LogSentry/
├── main.py
├── logsentry/
│   ├── __init__.py
│   ├── cli.py
│   ├── detector.py
│   ├── parser.py
│   └── report.py
├── tests/
│   ├── __init__.py
│   ├── test_detector.py
│   └── test_parser.py
├── .gitignore
├── LICENSE
└── README.md
```

## Running Tests

```bash
python3 -m unittest discover -s tests -v
```

## Security Note

LogSentry is intended for defensive security monitoring, education, and analysis of logs from systems you own or are authorized to monitor.

## License

This project is licensed under the MIT License.
