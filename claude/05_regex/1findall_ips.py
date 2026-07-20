# Output:
# Failed login for root from 10.0.0.9
# Accepted login for flamy from 10.0.0.9
# failed login for john from 10.0.0.8
# Failed login for root from 10.0.0.7
# Failed login for admin from 10.0.0.6
# Connection from 10.0.0.1 to 172.16.0.1 on port 443
# Connection from 10.0.0.2 to 172.16.0.2 on port 443
# Connection from 10.0.0.3 to 172.16.0.3 on port 443


import re

with open('sample.log', 'r') as f:
    for line in f:
        match = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        print(match)


# Output:
# ['10.0.0.9']                                                                                                    
# ['10.0.0.9']                                                                                                    
# ['10.0.0.8']                                                                                                    
# ['10.0.0.7']                                                                                                    
# ['10.0.0.6']                                                                                                    
# ['10.0.0.1', '172.16.0.1']                                                                                      
# ['10.0.0.2', '172.16.0.2']                                                                                      
# ['10.0.0.3', '172.16.0.3']                                                                                      

