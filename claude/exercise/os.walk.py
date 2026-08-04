import os

log_path = "/home/flamy/logs"
failed_count = 0

# FIND FAILED LOGINS
for dirpath, dirnames, filenames in os.walk(log_path):
    for filename in filenames:
        if filename.endswith(".log"):
            full_path = os.path.join(dirpath, filename)
            with open(full_path, "r") as f:
                for line in f:
                    if "Failed password" in line:
                        failed_count += 1
print("Failed login attempts:", failed_count)
# Output:
# Failed login attempts: 8                                                                                               
# Reading: /home/flamy/logs/host1/auth.log                                                                               
# 2026-07-21 14:32:01 Failed password for admin from 10.0.0.9                                                            
# 2026-07-21 14:32:03 Failed password for root from 10.0.0.9                                                             
# 2026-07-21 14:32:05 Failed password for admin from 10.0.0.9                                                            
# 2026-07-21 09:15:44 Accepted password for jsmith from 10.0.0.2                                                         
# 2026-07-21 14:32:07 Failed password for root from 10.0.0.9                                                             


# EXAMPLE TWO
log_path = "/home/flamy/logs"

for dirpath, dirnames, filenames in os.walk(log_path):
    for filename in filenames:
        if filename.endswith(".log"):
            full_path = os.path.join(dirpath, filename)
            print("Reading:", full_path)
            with open(full_path, "r") as f:
                for line in f:
                    print(line.strip())
# Output:
# Reading: /home/flamy/logs/host2/auth.log                                                                               
# 2026-07-21 15:01:12 Failed password for admin from 10.0.0.7                                                            
# 2026-07-21 15:01:15 Failed password for root from 10.0.0.7                                                             
# 2026-07-21 16:22:03 Failed password for admin from 10.0.0.5                                                            
# 2026-07-21 14:32:10 Failed password for admin from 10.0.0.9                                                            
