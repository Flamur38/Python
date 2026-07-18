import re

logs = [
    'Failed login from 10.0.0.9',
    'System rebooted',               # no IP on this line
    'Failed login from 10.0.0.6',
    'Failed login from 10.0.0.5',
    'System updated'
]

for lines in logs:
    try:
        match = re.search(r'\d+\.\d+\.\d+\.\d+', lines)
        print(match.group())
    except AttributeError:
        print('No IP on this line')




