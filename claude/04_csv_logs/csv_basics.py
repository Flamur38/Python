
with open('sample.csv', 'r') as f:
    for line in f:
        line = line.strip().split(',') # .strip() removes the newline 
        username = line[1]
        action = line[3]
        print(username, action)
