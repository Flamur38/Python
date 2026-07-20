# flagged_ips.txt
# Suspicious IPs: 10.0.0.9
# Suspicious IPs: 10.0.0.8
# Suspicious IPs: 10.0.0.7
# Suspicious IPs: 10.0.0.6

# sample.log
# Failed login for root from 10.0.0.9
# Accepted login for flamy from 10.0.0.9
# failed login for john from 10.0.0.8
# Failed login for root from 10.0.0.7
# Failed login for admin from 10.0.0.6
# Connection from 10.0.0.1 to 172.16.0.1 on port 443
# Connection from 10.0.0.2 to 172.16.0.2 on port 443
# Connection from 10.0.0.3 to 172.16.0.3 on port 443

import re

with open('flagged_ips.txt', 'w') as out:
    with open('sample.log', 'r') as f:
        for line in f:
            if 'failed' in line.lower():
                match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                for ip in match:
                    out.write('Suspicious IPs: {}\n'.format(ip))

print('Done - results written to flagged_ips.txt')


# Ouput:
# Done - results written to flagged_ips.txt
# # flagged_ips.txt
# # Suspicious IPs: 10.0.0.9
# # Suspicious IPs: 10.0.0.8
# # Suspicious IPs: 10.0.0.7
# # Suspicious IPs: 10.0.0.6

