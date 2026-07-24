import os

filepath = '/home/flamy/logs'
counts = 0

if not os.path.exists(filepath):
    print('Directory does not exist: {}'.format(filepath))
else:
    # os.walk() recursively visits every directory under 'filepath'.
    # It returns:
    #   dirpath   -> current directory being visited
    #   dirnames  -> subdirectories inside the current directory
    #   filenames -> files inside the current directory
    for dirpath, dirnames, filenames in os.walk(filepath):

        # Process every file in the current directory.
        for filename in filenames:

            # Only process files with a '.log' extension.
            if filename.endswith('.log'):

                # Join the directory path and filename into one full path.
                full_path = os.path.join(dirpath, filename)

                counts += 1
                print('Found .log file: {}'.format(full_path))
    print('Total .log files found: {}'.format(counts))
