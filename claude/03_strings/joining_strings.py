# sample.log
# Failed login for root from 10.0.0.9
# Accepted login for flamy from 10.0.0.9
# failed login for john from 10.0.0.8
# Failed login for root from 10.0.0.7
# Failed login for admin from 10.0.0.6


with open('sample.log', 'r') as f:
    for line in f:
        if 'failed' in line.lower():
            parts = line.split()
            username = parts[3]
            ip = parts[5]
            result = ','.join([username, ip])
            print(result)


# Output:
# root,10.0.0.9                                                                                                   
# john,10.0.0.8                                                                                                   
# root,10.0.0.7                                                                                                   
# admin,10.0.0.6
