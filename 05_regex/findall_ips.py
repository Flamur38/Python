import re

with open('sample_one.log', 'r') as f:
    for line in f:
        match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        print(match)
