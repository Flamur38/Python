count = 0

with open('sample.log', 'r') as f:
    for line in f:
        if 'failed' in line.lower():
            count += 1
            print(line.strip())
print()
print('Total Failed logins: {}'.format(count))
