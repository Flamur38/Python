
# a function that checks if an ip address is suspicious
def check_ip(ip):
    if ip == '10.0.0.9':
        print('suspicious message {}'.format(ip))
    else:
        print('clean message {}'.format(ip))


check_ip('10.0.0.9')
check_ip('192.168.1.45')
check_ip('192.168.1.55')
