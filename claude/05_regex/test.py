import re

line = 'Connection from port 4444 detected'

match = re.search(r'\d+', line)
print(match.group())

# Output: 4444



