import os
import json

def getFiles() -> list[str]:
    currentWorkDirectory = os.getcwd()
    return os.listdir(currentWorkDirectory)

def hasIdNumber(user_input: str) -> int:
    id = 0

    for number in user_input:
        if number.isdigit():
            id = int(number)
    
    return id

def handleAllListCommands(fileName: str, user_input: str):
    fileOpen = open(fileName)
    fileData = json.load(fileOpen)

    for tasks in fileData['tasks']:
        tasks_status = tasks['status']

        match user_input:
            case 'list':
                print(f'tasks in list: {tasks}')
            case 'list done':
                if tasks_status == "done":
                    print(f'tasks done: {tasks}')
            case 'list todo':
                if tasks_status == "todo":
                    print(f'tasks todo: {tasks}')
            case 'list in-progress':
                if tasks_status == "in-progress":
                    print(f'In pogress tasks: {tasks}')
            case _:
                print("You entered a command not found, try again")

def markTodosStatus(fileName: str, taskID: int):
    fileOpen = open(fileName)
    fileData = json.load(fileOpen)

    for tasks in fileData['tasks']:
        tasksID = tasks['id']
        
        if tasksID == taskID:
            print(tasks)


jsonFile = ""
currentFiles = getFiles()
tasks_list = {}

for files in currentFiles:
    if ".json" in files:
        jsonFile = str(files)
   

while jsonFile != "":
    print("task-cli")
    user_input = input("\033[1A\033[10C")

    if "list" in user_input:
        handleAllListCommands(jsonFile, user_input)
    elif "mark" in user_input:
        id = hasIdNumber(user_input)
        markTodosStatus(jsonFile, id)
