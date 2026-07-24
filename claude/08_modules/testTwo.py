
import os 

for dirpath, dirnames, filenames in os.walk('/home/flamy/logs'):
    print(dirpath)      # str   - the directory currently being visited
    print(dirnames)     # list  - subdirectory names inside it
    print(filenames)    # list  - file names inside it




