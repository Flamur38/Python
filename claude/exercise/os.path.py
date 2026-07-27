import os

for dirpath, dirnames, filenames in os.walk("/var/log"):

    for filename in filenames:

        if filename.endswith(".log"):

            full_path = os.path.join(dirpath, filename)

            print(full_path)
