
import re

line = '2026-07-21 14:32:01 Failed password for admin from 10.0.0.9'

match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
try:
    ip = match.group()
    print(ip)
except AttributeError:
    pass



