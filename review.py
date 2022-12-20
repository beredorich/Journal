from datetime import date, timedelta
import os
import sys

import numpy
today = date.today()

month = today.strftime("%B")
print(month)

folder = os.listdir()
path = os.getcwd()
for root, dirs, files in os.walk(path):
    for dir in dirs:
        if dir.__contains__(month):
            monthFolder = (path + '\\' +  dir)

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
filePath = monthFolder + "\\" + fileChosen

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
tasks = lastDay[0]

for task in tasks:
    #Extract []Tasks only
    review = ''
    if '[]' in task:
        while (review != 'y') and (review != 'Y') and (review != 'n') and (review != 'N'):
            os.system('cls')
            print(task)
            review = input('Done?\t (y/n):\t')
    if "y" in review:
        task.replace("[]", "[x]")
    

print('Review Complete!')
print(tasks)


