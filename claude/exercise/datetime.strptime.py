from datetime import datetime

# Parse timestamps and calculate attack duration
logs = [
    "2026-07-21 14:32:01 Failed password for admin from 10.0.0.9",
    "2026-07-21 14:35:01 Failed password for root from 10.0.0.9",
    "2026-07-21 15:01:12 Failed password for root from 10.0.0.7"
]

timestamps = []

for line in logs:
    time = line[:19]
    parsed = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    timestamps.append(parsed)

first_attempt = min(timestamps)
last_attempt = max(timestamps)

print(f'First attempt:\n{first_attempt}\n')
print(f'Last attempt:\n{last_attempt}\n')

total_seconds = (max(timestamps) - min(timestamps)).total_seconds()
print('Duration:\n{}'.format(total_seconds))
