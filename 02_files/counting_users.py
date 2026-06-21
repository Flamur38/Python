
count = {}

with open('sample.log', 'r') as f:
    for line in f:
        if 'failed' in line.lower():
            parts = line.split()[3]
            if parts in count:
                count[parts] += 1
            else:
                count[parts] = 1
print(count)

            


            
    
