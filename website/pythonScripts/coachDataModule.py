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

def sortCoaches(data):
    coachList=[]

    with open('./' + str(data) + '/coaches.csv', 'r', newline='') as coachCSV:
        coaches = csv.reader(coachCSV, delimiter=',', quotechar='|')
        for coach in coaches:
            coachList.append(coach)
        coachCSV.close()

    for i in range(len(coachList)): 
      
        min_idx = i 
        for j in range(i+1, len(coachList)): 
            if coachList[min_idx][3] > coachList[j][3]: 
                min_idx = j 
              
        coachList[i], coachList[min_idx] = coachList[min_idx], coachList[i] 

    with open('./' + str(data) + '/coaches.csv', 'w', newline='') as csvfile:
        csvData = csv.writer(csvfile, delimiter=',', quotechar='|')
        for coach in coachList:

            csvData.writerow([str(line)])

        csvfile.close()

def createFile(data):
    with open('./' + str(data) + '/coaches.csv', 'x', newline='') as newCsv:
        newCsv.close()
        pass

def writeData(data, information):
    if checkFile(data) == False: 
        createFile(data)

    with open('./' + str(data) + '/coaches.csv', 'a', newline='') as csvfile:
        csvData = csv.writer(csvfile, delimiter=',', quotechar='|')
        for line in information:

            coachID = generateIndex(line[0])

            print(information)
            csvData.writerow([str(line + coachID)])
        csvfile.close()

def generateIndex(info):
    return hash(info)