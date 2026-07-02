import re

with open('sample.log', 'r') as f:
    for line in f:
        match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        print(match)
