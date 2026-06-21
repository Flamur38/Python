
with open('sample.log', 'r') as f:
    for line in f:
        if line.startswith('Failed'):
            parts = line.split()[5]
            print(line.replace(parts, 'REDACTED'))

