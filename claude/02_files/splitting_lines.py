
with open('sample.log', 'r') as f:
    for line in f:
        if 'failed' in line.lower():
            parts = line.split()
            print(parts[3], parts[5])

