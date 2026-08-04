from collections import Counter
import re
failed_ips = [
    "10.0.0.9",
    "10.0.0.9",
    "10.0.0.7",
    "10.0.0.9",
    "10.0.0.5"
]
counts = Counter(failed_ips)    # Option ONE

for ip, num in counts.items():
    print('{} -> {}'.format(ip, num))
# Output:
# 10.0.0.9 -> 3                                                                                                          
# 10.0.0.7 -> 1                                                                                                          
# 10.0.0.5 -> 1
# ---

# Version two:
print('---') 
counts = Counter()              # Option TWO  

logs = [
    'Failed password for 10.0.0.9',
    'Failed password for 10.0.0.9',
    'Failed password for 10.0.0.7'
]
for line in logs:
    if 'Failed password' in line:
        match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        ip = match.group()
        counts[ip] += 1

for ip, num in counts.items():
    print('{} -> {}'.format(ip, num))
    
top_ip, attempts = counts.most_common(1)[0]
print('Most common IP: {} -> {}'.format(top_ip, attempts))

# Output:
# 10.0.0.9 -> 2                                                                                                          
# 10.0.0.7 -> 1                                                                                                          
# Most common IP: 10.0.0.9 -> 2
