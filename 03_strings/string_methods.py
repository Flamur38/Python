
line = 'Failed login for root from 10.0.0.9'

print(line.startswith('Failed')) # True
print(line.endswith('9'))        # True

print(line.replace('root', 'REDACTED'))
# Failed login for REDACTED from 10.0.0.9

