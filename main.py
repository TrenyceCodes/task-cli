import os
import json

def getFiles() -> list[str]:
    currentWorkDirectory = os.getcwd()
    return os.listdir(currentWorkDirectory)


def handleAllListCommands(fileName: str, user_input: str):
    fileOpen = open(fileName)
    fileData = json.load(fileOpen)

    for tasks in fileData['tasks']:
        todo_status = tasks['status']

        match user_input:
            case 'list':
                print(tasks)
            case 'list done':
                if todo_status == "done":
                    print(tasks)
            case 'list todo':
                if todo_status == "todo":
                    print(tasks)
            case 'list in-progress':
                if todo_status == "in-progress":
                    print(tasks)
            case _:
                print("You entered a command not found, try again")

jsonFile = ""
currentFiles = getFiles()

for files in currentFiles:
    if ".json" in files:
        jsonFile = str(files)
   

while jsonFile != "":
    print("task-cli")
    user_input = input("\033[1A\033[10C")
    handleAllListCommands(jsonFile, user_input)
