from collections import Counter

counts = Counter(['10.0.0.9', '10.0.0.7', '10.0.0.9', '10.0.0.9', '10.0.0.5', '10.0.0.7'])
print(counts.most_common(3))                # top 3, sorted by count descending
# [('10.0.0.9', 3), ('10.0.0.7', 2), ('10.0.0.5', 1)]

for ip, hits in counts.most_common(3):      # unpack each pair in the loop
    print('{}: {} attempts'.format(ip, hits))
    
# 10.0.0.9: 3 attempts                                                                                                   
# 10.0.0.7: 2 attempts                                                                                                   
# 10.0.0.5: 1 attempts


