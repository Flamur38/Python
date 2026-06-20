
def check_ip(ip):
    if ip == '10.0.0.9':
        return 'suspicious'
    else:
        return 'clean'


ip_one = check_ip('10.0.0.9')
ip_two = check_ip('192.168.1.45')
ip_three = check_ip('192.168.1.55')

print('{}'.format(ip_one))
print('{}'.format(ip_two))
print('{}'.format(ip_three))
