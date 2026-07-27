# auth_ts.log
# 2026-07-21 14:32:01 Failed password for admin from 10.0.0.9
# 2026-07-21 14:32:03 Failed password for root from 10.0.0.9
# 2026-07-21 14:32:05 Failed password for admin from 10.0.0.9
# 2026-07-21 09:15:44 Accepted password for jsmith from 10.0.0.2
# 2026-07-21 14:32:07 Failed password for root from 10.0.0.9
# 2026-07-21 14:32:10 Failed password for admin from 10.0.0.9
# 2026-07-21 15:01:12 Failed password for admin from 10.0.0.7
# 2026-07-21 15:01:15 Failed password for root from 10.0.0.7
# 2026-07-21 16:22:03 Failed password for admin from 10.0.0.5
from collections import Counter
import re

filename = '/home/flamy/projects/Python/claude/08_modules/auth_ts.log'
counts = Counter()

try:
    with open(filename, 'r') as f:
        for line in f:

            if 'Failed password' in line:

                match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

                try:
                    ip = match.group()
                    counts[ip] += 1

                except AttributeError:
                    continue


    if counts:
        print('Top offenders:')

        for ip, hits in counts.most_common(3):
            print('{}: {} attempts'.format(ip, hits))

        print('Total unique IPs: {}'.format(len(counts)))

        for ip, hits in counts.items():
            if hits >= 5:
                print('ALERT: {} has {} failed attempts'.format(ip, hits))


except FileNotFoundError:
    print('File not found: {}'.format(filename))

