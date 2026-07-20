# sample.log
# Failed login for root from 10.0.0.9
# Accepted login for flamy from 10.0.0.9
# failed login for john from 10.0.0.8
# Failed login for root from 10.0.0.7
# Failed login for admin from 10.0.0.6


# Find and Slice
with open('sample.log', 'r') as f:
    for line in f:
        position = line.find('from') # returns the index    
        ip_part = line[position + 5:]  # slice out the part after 'from'
        print(ip_part)                  
        
# Output:
# 10.0.0.9                                                                                                        
# 10.0.0.9                                                                                                        
# 10.0.0.8                                                                                                        
# 10.0.0.7                                                                                                        
# 10.0.0.6
        

