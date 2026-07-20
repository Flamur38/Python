# sample.csv
# 2026-06-21 10:01:00,root,10.0.0.9,Failed
# 2026-06-21 10:01:00,admin,10.0.0.9,Failed
# 2026-06-21 10:01:00,flamy,10.0.0.9,Accepted
# 2026-06-21 10:01:00,root,10.0.0.9,Failed
# 2026-06-21 10:01:00,root,10.0.0.9,Failed


import csv

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line[1], line[3])


# Output:
# root Failed                                                                                                     
# admin Failed                                                                                                    
# flamy Accepted                                                                                                  
# root Failed                                                                                                     
# root Failed                                                                                                     

