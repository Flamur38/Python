from collections import Counter

counts = Counter({
    "10.0.0.9": 5,
    "10.0.0.7": 2,
    "10.0.0.5": 1,
    "10.0.0.12": 3
})

for ip, attempts in counts.items():

    if attempts >= 3:
        print('ALERT: {} - {} failed attempts'.format(ip, attempts))

    


