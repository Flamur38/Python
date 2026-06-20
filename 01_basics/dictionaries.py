
event = {                   
        'user': 'flamy',        # 'key': value
        'src_ip': '192.168.1.45',
        'action': 'Accepted password for flamy',
        }

# accessing value by its key name in [] instead of index number.
print(event['user'])   # flamy     
print(event['src_ip']) # 192.168.1.45

print()

event['dst_ip'] = '10.0.0.9'    # adding a new key to the dictionary
print('The new added key {}'.format(event['dst_ip']))


