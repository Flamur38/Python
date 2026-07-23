
import os

files = os.listdir('/home/flamy/')              # return a LIST of names in that directory
print(files[:3])
# ['snap', '.fehbg', 'Templates']


path = '/var/log/auth.log'
if os.path.exists(path):                        # returns True or False
    print('Found {}'.format(path))
else:
    print('Missing {}'.format(path))            # Missing /var/log/auth.log

print()

log_dir = '/home/flamur/logs'
path = os.path.join(log_dir, 'auth.log')   # joins with the right separator
print(path)
# /home/flamur/logs/auth.log
