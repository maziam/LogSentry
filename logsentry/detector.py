def count_failed_logins(records):
    counts={}
    for r in records:
        if r["event"] == "Failed":
            ip = r["ip"]
            counts[ip] = counts.get(ip, 0) + 1
    return counts

def detect_suspicious_ips(counts, threshold):
    return {ip:n for ip,n in counts.items() if n >= threshold}
