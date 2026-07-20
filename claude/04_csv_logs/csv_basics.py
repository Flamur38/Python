# sample.csv:
# 2026-06-21 10:01:00,root,10.0.0.9,Failed
# 2026-06-21 10:01:00,admin,10.0.0.9,Failed
# 2026-06-21 10:01:00,flamy,10.0.0.9,Accepted
# 2026-06-21 10:01:00,root,10.0.0.9,Failed
# 2026-06-21 10:01:00,root,10.0.0.9,Failed


with open('sample.csv', 'r') as f:
    for line in f:
        line = line.strip().split(',') # .strip() removes the newline 
        username = line[1]
        action = line[3]
        print(username, action)


# Output:
# root Failed                                                                                                     
# admin Failed                                                                                                    
# flamy Accepted                                                                                                  
# root Failed                                                                                                     
# root Failed 
