
# Find and Slice
with open('sample.log', 'r') as f:
    for line in f:
        position = line.find('from') # returns the index    
        ip_part = line[position + 5:]  # slice out the part after 'from'
        print(ip_part)                  
        
        
        

