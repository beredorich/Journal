from datetime import date, timedelta
import os
import sys

today = date.today()

month = today.strftime("%B")
print(month)

folder = os.listdir()
path = os.getcwd()
for root, dirs, files in os.walk(path):
    for dir in dirs:
        if dir.__contains__(month):
            monthFolder = (path + '//' +  dir)

while True:
    try: 
        print("Choose Week:")
        i = 1
        for week in os.listdir(monthFolder):
            print(str(i) + ") " + week)
            i = i + 1
        print(str(i) + ") " + "Exit")
        print("------------")
        choice = int(input())
        if choice < i and choice > 0:
            break
        elif choice is i:
            sys.exit(0)
        else:
            print("\nERROR. Enter valid Int choice.\n")
    except ValueError:
        print("\nERROR. Enter valid Int choice.\n")




fileChosen = (os.listdir(monthFolder))[choice-1]
filePath = monthFolder + "//" + fileChosen

with open(filePath) as file:
    lines = file.readlines()


breakIndex = [i for i, x in enumerate(lines) if x == "-----------------------------------------\n"]
endLine = len(lines)
breakIndex.append(endLine)



d = {}
for i in range(len(breakIndex)):
    d[i] = []


for i in range(len(d)):
    dayArray = []
    dayArray.append(lines[breakIndex[i-1]: breakIndex[i]])
    d[i] = dayArray
    

lastDay = d[len(breakIndex)-1]
done = []
unfinished = []

tasks = lastDay[0]
for task in tasks: 
    if '[x]' in task:
        done.append(task)
    if '[]' in task:
        unfinished.append(task)

completedTasks = str(len(done))
unfinishedTasks = str(len(unfinished))

with open(filePath, 'a') as writer:
    
    writer.write("\nCOMPLETED TASKS: " + completedTasks + "\n")     
    writer.write("TASKS TO COMPLETE: " + unfinishedTasks + "\n")
    writer.write("-----------------------------------------\n")
    tommorow = today + timedelta(1)
    writer.write((tommorow.strftime("%d %b %y")).upper() + "\n\n")

    for unfinishedTask in unfinished:
        writer.write(unfinishedTask)
    