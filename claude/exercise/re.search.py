import re

# Extract IPs
line = '2026-07-21 14:32:01 Failed password for admin from 10.0.0.9'
match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

try:
    ip = match.group()
    print(ip)
except AttributeError:
    pass

# Filter logins + Extract IPs
logs = [
    "2026-07-21 14:32:01 Failed password for admin from 10.0.0.9",
    "2026-07-21 14:32:03 Failed password for root from 10.0.0.9",
    "2026-07-21 14:35:10 Accepted password for jsmith from 10.0.0.2",
    "2026-07-21 15:01:12 Failed password for root from 10.0.0.7",
    "2026-07-21 15:10:22 System rebooted"
]
failed_ips = []

for line in logs:
    if 'Failed password' in line:
        match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

        try:
            ip = match.group()
        except AttributeError:
            continue

        failed_ips.append(ip)
print(failed_ips)
            

