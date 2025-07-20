from abc import update_abstractmethods
import os
import json
from datetime import datetime
from typing import dataclass_transform

from Tasks import Tasks

def getFiles() -> list[str]:
    currentWorkDirectory = os.getcwd()
    return os.listdir(currentWorkDirectory)

def hasId(user_input: str) -> int:
    id = 0

    for number in user_input:
        if number.isdigit():
            id = int(number)
    
    return id

def totalTasks(fileName: str) -> int:
    total = 0
    with open(fileName, "r+") as file:
        fileData = json.load(file)
        tasks = fileData["tasks"]
        total = len(tasks)

    return total
    

def handleAllListCommands(fileName: str, user_input: str):
    fileOpen = open(fileName, "r")
    fileData = json.load(fileOpen)

    for tasks in fileData['tasks']:
        tasks_status = tasks['status']

        match user_input:
            case 'list':
                print(f'{tasks}')
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
    
    fileOpen.close()

def markTaskInProgress(fileName: str, taskID: int):
    with open(fileName, "r+") as file:
        fileData = json.load(file)

        for tasks in fileData["tasks"]:
            tasksID = tasks.get("id")
            
            if tasksID == taskID:
                tasks["status"] = "in-progress"

    with open(fileName, "w") as file: 
        json.dump(fileData, file, indent=4)
    
def markTaskDone(fileName: str, taskID: int):
    with open(fileName, "r") as file:
        fileData = json.load(file)

        for tasks in fileData["tasks"]:
            tasksID = tasks.get("id")

            if tasksID == taskID:
                tasks["status"] = "done"

    with open(fileName, "w") as file:
        json.dump(fileData, file, indent=4)

def deleteTask(fileName: str, taskID: int):
    with open(fileName, 'r+') as file:
        fileData = json.load(file)
        
        for tasks in fileData["tasks"]:
            if tasks["id"] == taskID:
                tasks["status"] = "in-progress"
          
    with open(fileName, 'w') as file:
        json.dump(fileData, file, indent=4)

def addTask(fileName: str, description: str):
    with open(fileName, 'r+') as file:
        new_data = {
            "id": totalTasks(fileName) + 1,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().strftime('%Y-%m-%d %H-%M-%S'),
            "updatedAt": "",
        }
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'emp_details' list
        file_data["tasks"].append(new_data)
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)

def checkForDescription(user_input: str) -> str:
    description = ''
    endStr = user_input.rfind('"')
    beginningStr = user_input.index('"')
   
    while beginningStr < endStr:
        beginningStr += 1
        description += user_input[beginningStr]

    return description.replace('"', "")


jsonFile = ""
currentFiles = getFiles()
tasks_list = {}

for files in currentFiles:
    if ".json" in files:
        jsonFile = str(files)
   

while jsonFile != "":
    print("task-cli")
    user_input = input("\033[1A\033[10C")

    if "add" in user_input:
        taskDescription = checkForDescription(user_input)
        addTask(jsonFile, taskDescription)
    elif "list" in user_input:
        handleAllListCommands(jsonFile, user_input)
    elif "mark-in-progress" in user_input:
        id = hasId(user_input)
        markTaskInProgress(jsonFile, id)
    elif "mark-done" in user_input:
        id = hasId(user_input)
        markTaskDone(jsonFile, id)
    elif "delete" in user_input:
        id = hasId(user_input)
        deleteTask(jsonFile, id)
    else:
        print("Command not found try again")
        continue
