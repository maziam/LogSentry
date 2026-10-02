def print_report(counts, suspicious, threshold):
    print("Threshold:", threshold)
    print("\nFailed Login Counts:")
    for ip,n in counts.items():
        print(f"{ip} -> {n}")
    print("\nSuspicious IPs:")
    if not suspicious:
        print("None")
    for ip,n in suspicious.items():
        print(f"{ip} -> SUSPICIOUS -> {n}")
