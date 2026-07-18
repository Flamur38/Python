
with open('sample.log', 'r') as f:
    for line in f:
        if 'failed' in line.lower():
            parts = line.split()
            username = parts[3]
            ip = parts[5]
            result = ','.join([username, ip])
            print(result)


