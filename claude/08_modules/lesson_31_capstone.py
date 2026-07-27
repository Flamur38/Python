import os
import re
from collections import Counter
from datetime import datetime

filesPath = '/home/flamy/logs/'

counts = Counter()
timestamps = []
files_scanned = 0

if not os.path.exists(filesPath):
    print('Path does not exists: {}'.format(filesPath))

else:
    for dirpath, dirnames, filenames in os.walk(filesPath):

        for filename in filenames:

            if filename.endswith('.log'):

                full_path = os.path.join(dirpath, filename)
                files_scanned += 1

                try:
                    with open(full_path, 'r') as f:
                        for line in f:
                            if 'Failed password' in line:
                                match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

                                try:
                                    ip = match.group()
                                except AttributeError:
                                    continue

                                ts = line[:19]

                                try:
                                    parsed = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
                                except ValueError:
                                    continue


                                counts[ip] += 1
                                timestamps.append(parsed)

                except FileNotFoundError:
                    print('File does not exists: {}'.format(full_path))


# Report
if len(counts) == 0:
    print('No failed logins found')

else:
    print('\n=== REPORT ===')
    print('Files scanned: {}'.format(files_scanned))
    print('Total failed attempts: {}'.format(sum(counts.values())))
    print('\nTop 3 attacking IPs:')
    for ip, amount in counts.most_common(3):
        print('{} -> {}'.format(ip, amount))

    print('\nUnique IP count: {}'.format(len(counts)))
    start = min(timestamps)
    end = max(timestamps)

    print('\nTime span: {} to {}'.format(start, end))

    seconds = (end - start).total_seconds()
    
    print('Duration: {} seconds'.format(seconds))

    print('\nAlerts:')

    for ip, amount in counts.items():

        if amount >= 3:
            print('ALERT: {} - {} failed attempts'.format(ip, amount))

