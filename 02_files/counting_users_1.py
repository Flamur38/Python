
# This functions does count the number of failed logins
def counting_failed_logins(filename):
    counts = {}
    with open(filename, 'r') as f:
        for line in f:
            if 'failed' in line.lower():
                parts = line.split()[3]
                if parts in counts:
                    counts[parts] += 1
                else:
                    counts[parts] = 1
    return counts

# Take some filenames as arguments  
result = counting_failed_logins('sample.log')
result_1 = counting_failed_logins('sample_1.log')

# Print the results
print(result)
print(result_1)
