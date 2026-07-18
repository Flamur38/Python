
line = '2026-06-21 10:01:00,root,10.0.0.9,Failed'
fields = line.split(',')
print(fields)
# ['2026-06-21 10:01:00', 'root', '10.0.0.9', 'Failed']                                                                  


print(fields[1]) # root
print(fields[2]) # 10.0.0.9
