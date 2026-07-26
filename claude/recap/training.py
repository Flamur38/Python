from re import findall
import re


print('Drill 1: Lists + for loop + if/or(basics)')
# Lists + for loop + if/or(basics)
ports = [22, 80, 443, 23, 3389, 21, 8080]
for port in ports:
    if port == 23 or port == 21 or port == 3389:
        print('Risky port found: {}'.format(port))
print('---')


print('Drill 2: dictionary + looping')
failed = {'root': 14, 'admin': 3, 'flamur': 1, 'svc_backup': 22}
for user, attempts in failed.items():
    if attempts > 5:
        print('{} -> {} fails'.format(user, attempts))
print('---')


print('Drill 3: function with return value')
def is_internal(ip):
    if ip.startswith('10') or ip.startswith('192.168'):
        return True
    else:
        return False
checkip_one = is_internal('10.0.0.9')
checkip_two = is_internal('82.0.0.9')
print(checkip_one)
print(checkip_two)
print('---')

        
print('Drill 4: string methods + slicing')
line = '2025-07-25T09:14:22 ssdh FAILED login user=root src=203.0.113.9'
position = line.find('user=')
start = position + 5                # option one
start = position + len('user=')     # option two
end = line.find(' ', start)
username = line[start:end]
print(username)
# using the .split() methods:
# user = line.split()[4]
# name = user.split('=')[1]
# print(name)
print('---')


print('Drill 5: reading + filtering + counting a file')
count = 0
with open('auth.log', 'r') as f:
    for line in f:
        if 'Failed' in line:
            count += 1
    print('{} Failed attempts'.format(count))
print('---')


print('Drill 6: csv split with the strip-before-split discipline')
row = ' 203.0.113.9 , root, 22 , FAILED \n'
parts = row.strip().split(',')
print(parts[0].strip())
print('---')


print('Drill 7: regex (re.search + IP pattern)')
line = "2025-07-25T09:14:22 sshd FAILED login user=root src=203.0.113.9"
match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
ip = match.group()
print(ip)
print('---')



# auth.log
# Failed password for admin from 10.0.0.9 port 22
# Accepted password for jsmith from 10.0.0.2 port 22
# Failed password for root from 10.0.0.9 port 22
# System rebooted
# Failed password for admin from 10.0.0.7 port 22
# Failed password for root from 10.0.0.9 port 22
print('Drill 8: the full pipeline + error handling + writing')
with open('auth.log', 'r') as f:
    with open('ips.txt', 'w') as out:
        for line in f:
            try:
                match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
                ip = match.group()
                out.write('IP found: {}\n'.format(ip))

            except AttributeError:
                print('no ip')

    
