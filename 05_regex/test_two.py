import re

line = 'Connection from 10.0.0.9 to 172.16.0.5 on port 443'

matches = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
print(matches)
# ['10.0.0.9', 172.16.0.5']


