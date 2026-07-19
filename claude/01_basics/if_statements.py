
ports = [21, 25, 443, 80, 4444, 9001]

for port in ports:
    if port == 4444 or port == 9001:
        print('Suspicious port found: {}'.format(port))
    else:
        print('Port {} looks normal'.format(port))

# Output:
# Port 21 looks normal                                                                                            
# Port 25 looks normal                                                                                            
# Port 443 looks normal                                                                                           
# Port 80 looks normal                                                                                            
# Suspicious port found: 4444                                                                                     
# Suspicious port found: 9001
