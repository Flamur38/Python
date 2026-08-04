import re
from collections import Counter
from datetime import datetime
logs = [
    "2026-07-21 14:32:01 Failed password for admin from 10.0.0.9",
    "2026-07-21 14:32:03 Failed password for root from 10.0.0.9",
    "2026-07-21 14:32:05 Failed password for admin from 10.0.0.9",
    "2026-07-21 15:01:12 Failed password for root from 10.0.0.7",
    "2026-07-21 16:22:03 Failed password for admin from 10.0.0.5",
    "2026-07-21 16:22:03 Accepted password for admin from 10.0.0.5",
]

# Create storage:
counts = Counter()
timestamps = []

for line in logs:
    if 'Failed password' in line:
        match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        if match:
            ip = match.group()

        counts[ip] += 1
        time = line[:19]
        parsed = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        timestamps.append(parsed)

first = min(timestamps)
last = max(timestamps)
duration = (max(timestamps) - min(timestamps)).total_seconds()

print('===== Report =====\n')

# Total attempts:
total_attempts = sum(counts.values())
print('Total failed attempts: {}\n'.format(total_attempts))

# Top Attacker:
print('Top attackers:') 
for ip, num in counts.most_common(3):
    print('{} -> {}'.format(ip, num))

print('\nFirst attempt:\n{}'.format(first))
print('\nLast attempt:\n{}'.format(last))
print('\nDuration: {} seconds'.format(duration))
print('\nAlerts:')

for ip, attempts in counts.items():
    if attempts >= 3:
        print('ALERT: {} - {} failed attempts'.format(ip, attempts))

# Output:
# ===== Report =====
#
# Total failed attempts: 5
#
# Top attackers:
# 10.0.0.9 -> 3
# 10.0.0.7 -> 1
# 10.0.0.5 -> 1
#
# First attempt:
# 2026-07-21 14:32:01
#
# Last attempt:
# 2026-07-21 16:22:03
#
# Duration: 6602.0 seconds
#
# Alerts:
# ALERT: 10.0.0.9 - 3 failed attempts

