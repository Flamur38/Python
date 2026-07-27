import os  

path = '/home/flamy/logs/'

# Get a list of all files and directories inside 'path'
logs = os.listdir(path)
print(logs)
# ['syslog.log', 'report.csv', 'auth.log', 'host1', 'kern.log', 'apache2', 'host2', 'notes.txt', 'nginx']


# Counter for the number of .log files found
total = 0

# Iterate through every item returned by os.listdir()
for name in logs:
    if name.endswith('.log'):

        # Build the full file path (e.g. /home/flamy/logs/auth.log)
        full_path = os.path.join(path, name)
        print('Found log file: {}'.format(full_path))
        total += 1

print('Total .log files found: {}'.format(total))
