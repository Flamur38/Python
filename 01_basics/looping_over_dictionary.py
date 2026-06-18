
event = {
        'user': 'flamy',        
        'src_ip': '192.168.1.45',
        'action': 'Accepted password for flamy',
        }


for key, value in event.items():    # .items() gives both key and value 
    if key == 'action':
        print('Event action: {}'.format(value))
    else:
        print('{}: {}'.format(key, value))

