import re                                        # regex, for pulling IPs out of log lines

log_file = 'auth.log'                            # input filename, written ONCE
report_file = 'failed_report.txt'                # output filename

counts = {}                                      # ip -> how many failed logins

try:
    with open(log_file) as f:                    # THIS is the line that can raise FileNotFoundError
        for line in f:
            if 'Failed password' in line:
                try:
                    match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
                    ip = match.group()           # raises AttributeError if match is None
                    counts[ip] = counts.get(ip, 0) + 1
                except AttributeError:
                    print('No IP on this line')

    with open(report_file, 'w') as out:          # still inside the try
        for ip, num in counts.items():
            out.write('{}: {}\n'.format(ip, num))
    print('Report written to {}'.format(report_file))

except FileNotFoundError:
    print('Log file not found: {}'.format(log_file))
