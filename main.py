import os
import json

currentWorkDirectory = os.getcwd()
currentFiles = os.listdir(currentWorkDirectory)
print(currentFiles)

for files in currentFiles:
    print(files)
