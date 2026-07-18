import re

with open('flagged_ips.txt', 'w') as out:
    with open('sample.log', 'r') as f:
        for line in f:
            if 'failed' in line.lower():
                match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                for ip in match:
                    out.write('Suspicious IPs: {}\n'.format(ip))

print('Done - results written to flagged_ips.txt')

