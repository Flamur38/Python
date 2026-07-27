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
            print("---")
