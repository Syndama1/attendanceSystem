import csv as csv
import os

class coachData:
    def __init__(self, coach, coachid):
        self.coach = coach
        self.coachid = coachid

def openFile(data):
    csvList = []

    with open('./' + str(data) + '/coaches.csv', newline='') as csvfile:
        csvData = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvData:
            csvList.append(row)

        return csvList

def checkData(data):
    coachInfo = openFile(data)

    print(coachInfo)

    if coachInfo == []: 
        return False 
    else:
        return True

def checkFile(data):
    if os.path.isfile('./' + str(data) + '/coaches.csv'):
        return checkData(data)
    else: 
        return False
