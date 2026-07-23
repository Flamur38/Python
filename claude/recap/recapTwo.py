# blocklist.txt:
# 10.0.0.9
# 10.0.0.7


filename = 'blocklist.txt'
ips = []

try:

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()        
            ips.append(line)

    print(ips)
    print(len(ips))


except FileNotFoundError:
    print('file does not exists')
