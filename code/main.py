#!/bin/bash
import os
import sys

from File import File

# Load files
myfiles = []
for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        myfiles.append(File(os.path.join(root, file)))

print(myfiles)