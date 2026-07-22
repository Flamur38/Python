import re
# Part A 
# A1. Format an alert line.
# Given these variables, print exactly: ALERT: admin failed login from 10.0.0.9 on port 22
user = 'admin'
ip = '10.0.0.9'
port = 22
print('ALERT: {} failed login from {} on port {}'.format(user, ip, port))

# ---

# A2. Flag suspicious ports.
# Loop over the list below. For each port, print <port> is a remote-access port only if it's 22, 23, or 3389.
ports = [80, 22, 443, 3389, 8080, 23]
for port in ports:
    if port == 22 or port == 23 or port == 3389:
        print('{} is a remote-access port'.format(port))
# ---

# Part B — Data wrangling
# B1. Count failed logins per IP (dictionary).
# Given the list below, build a dict that counts how many times each IP appears, 
# then print each IP with its count.
# Expected:
# 10.0.0.9 appears 3 times, 10.0.0.7 appears 2 times
lines = [
    'Failed login 10.0.0.9',
    'Failed login 10.0.0.7',
    'Failed login 10.0.0.9',
    'Failed login 10.0.0.9',
    'Failed login 10.0.0.7',
]

count = {}

for line in lines:
    if 'Failed' in line:              # Only process failed login events
        ip = line.split()[2]           # Extract the IP address from the log line
        
        if ip in count:                # Check if this IP already exists in dictionary
            count[ip] += 1             # Increase the existing counter by 1
        else:
            count[ip] = 1              # First occurrence of this IP, start counter at 1

parts = []

for ip, num in count.items():
    parts.append('{} appears {} times'.format(ip, num))  
    # Build a formatted string and store it in the list

print(', '.join(parts))                
# Join all list elements into one line separated by ", "

# Alternative:
# print('{} appears {} times'.format(ip, num), end=', ')
# Prints each result immediately without creating a list

# ---

# B2. Pull the username out of a field.
# From this line, extract just the username (admin) using either .split() or .find() + slicing — your call.
# should end up with: admin
line = 'ts=2026-07-21 user=admin action=login result=FAILED'

# Solution using .find()
position = line.find('user')      # Find where "user" starts
start = position + 5              # Skip "user="
end = line.find(' ', start)       # Find the next space
username = line[start:end]        # Extract the username
print(username)

# Solution using .split()
user = line.split()[1]            # Get "user=admin"
name = user.split('=')[1]         # Get "admin"
print(name)

#---

# Part C — Mini capstone (combine everything)
# First, save this as auth.log in your working directory:

# Failed password for admin from 10.0.0.9 port 22
# Accepted password for jsmith from 10.0.0.2 port 22
# Failed password for root from 10.0.0.9 port 22
# System rebooted
# Failed password for admin from 10.0.0.7 port 22
# Failed password for root from 10.0.0.9 port 22
counts = {}

# Phase 1: Read log file and collect failed login statistics
with open('auth.log', 'r') as f:
    for line in f:
        try:
            if 'Failed password' in line:              # Only process failed login attempts
                
                match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                ip = match.group(1)                    # Extract IP from regex match

                if ip in counts:
                    counts[ip] += 1                    # Increase existing IP counter
                else:
                    counts[ip] = 1                     # First time seeing this IP

        except AttributeError:
            print('No IP found')


# Phase 2: Write report file
with open('failed_report.txt', 'w') as out:
    for ip, count in counts.items():
        out.write('{}: {}\n'.format(ip, count))

