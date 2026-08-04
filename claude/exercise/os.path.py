import os

for dirpath, dirnames, filenames in os.walk("/var/log"):

    for filename in filenames:

        if filename.endswith(".log"):

            full_path = os.path.join(dirpath, filename)

            print(full_path)
            
            # Output:
            # /var/log/apport.log
            # /var/log/cloud-init-output.log
            # /var/log/cloud-init.log
            # /var/log/auth.log
            # /var/log/kern.log

