# blocklist.txt:
# 10.0.0.9
# 10.0.0.8
# 10.0.0.7
# 10.0.0.6
# 10.0.0.5


filename = 'blocklist.txt'
ips = []

try:
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()             # Remove leading/trailing whitespace and the trailing '\n'

            if line:                        # Skip empty lines ('') because an empty string is False
                ips.append(line)            # Add the cleaned IP address to the end of the list

    print('Loaded {} IPs'.format(len(ips))) # len() returns the number of items in the list
    print(ips)

except FileNotFoundError:
    print('Error: {} not found.'.format(filename))

