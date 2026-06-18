
ports = [21, 25, 443, 80, 4444, 23]

for port in ports:
    if port == 4444 or port == 23:
        print('Suspicious port found: {}'.format(port))
    else:
        print('Port {} looks normal'.format(port))
