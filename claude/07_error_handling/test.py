import re

lines = [
    'Failed login from 10.0.0.9',
    'System rebooted',              # no IP on this line
    'Failed loging from 10.0.0.7'
]

for line in lines:
    try:
        match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        print(match.group())
    except AttributeError:
        print('No IP found on this line')

# OUTPUT:
# 10.0.0.9
# No IP found on this line
# 10.0.0.7

