count = 0

with open('sample.log', 'r') as f:
    for line in f:
        if 'failed' in line.lower():
            count += 1
            print(line.strip()) 
print('Total Failed logins: {}'.format(count))


# Ouput:
# Failed login for root from 10.0.0.9                                                                             
# failed login for john from 10.0.0.8                                                                             
# Failed login for root from 10.0.0.7                                                                             
# Failed login for admin from 10.0.0.6                                                                            

