# auth_ts.log
# 2026-07-21 14:32:01 Failed password for admin from 10.0.0.9
# 2026-07-21 14:32:03 Failed password for root from 10.0.0.9
# 2026-07-21 14:32:05 Failed password for admin from 10.0.0.9
# 2026-07-21 09:15:44 Accepted password for jsmith from 10.0.0.2
# 2026-07-21 14:32:07 Failed password for root from 10.0.0.9
# 2026-07-21 14:32:10 Failed password for admin from 10.0.0.9

from datetime import datetime

filename = 'auth_ts.log'
attempts = []

try:
    with open(filename, 'r') as f:
        for line in f:

            if 'Failed password' in line:

                # The timestamp is always the first 19 characters:
                # YYYY-MM-DD HH:MM:SS
                timestamp = line[:19]

                # Convert the timestamp string into a datetime object.
                parsed = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

                # Store each parsed datetime in a list.
                attempts.append(parsed)

        print('Failed attempts found: {}'.format(len(attempts)))

        # Continue only if at least one failed attempt was found.
        if attempts:

            # min() and max() return the earliest and latest datetime.
            # This works even if the log file is not in chronological order.
            first = min(attempts)
            last = max(attempts)

            print('First attempt: {}, Last attempt: {}'.format(first, last))

            # Subtracting two datetime objects returns a timedelta object.
            span = last - first

            # Convert the timedelta into seconds.
            print('The total span from first to last: {} seconds'.format(span.total_seconds()))

            # Alert if there were at least 5 failed attempts within 60 seconds.
            if len(attempts) >= 5 and span.total_seconds() <= 60:
                print('ALERT: possible brute force')

except FileNotFoundError:
    print('File not found: {}'.format(filename))
