# sameple.log:
# Failed login for root from 10.0.0.9
# Accepted login for flamy from 10.0.0.9
# failed login for john from 10.0.0.8
# Failed login for root from 10.0.0.7
# Failed login for admin from 10.0.0.6

with open('sample.log', 'r') as f:
    for line in f:
        if 'failed' in line.lower():
            parts = line.split()
            print(parts[3], parts[5])


# Output:
# root 10.0.0.9                                                                                                   
# john 10.0.0.8                                                                                                   
# root 10.0.0.7                                                                                                   
# admin 10.0.0.6

