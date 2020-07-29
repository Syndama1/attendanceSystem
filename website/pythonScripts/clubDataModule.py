import csv as csv
import os

class clubData:
    def __init__(self, title, coach, description):
        self.title = title
        self.coach = coach
        self.description = description

def openFile(data):
    csvList = []

    with open('./' + str(data) + '/clubInfo.csv', newline='') as csvfile:
        csvData = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvData:
            csvList.append(row)

        return csvList

def checkData(data):
    clubInfo = openFile(data)

    print(clubInfo)

    if clubInfo == []: 
        return False 
    else:
        return True

def checkFile(data):
    if os.path.isfile('./' + str(data) + '/clubInfo.csv'):
        return checkData(data)
    else: 
        return False

def createFile(data):
    with open('./' + str(data) + '/clubInfo.csv', 'x', newline='') as newCsv:
        newCsv.close()
        pass

def writeData(data, information):
    if checkFile(data) == False: 
        createFile(data)

    with open('./' + str(data) + '/clubInfo.csv', 'w', newline='') as csvfile:
        csvData = csv.writer(csvfile, delimiter=',', quotechar='|')
        for line in information:
            print(information)
            csvData.writerow([str(line)])
        csvfile.close()