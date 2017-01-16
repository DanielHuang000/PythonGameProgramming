import csv
import datetime

def OriGoogleData(fileName):
    """
    Read the original data in google calssroom
    :param fileName: name of the file
    :return: all data in list
    """
    # open the file
    gcFile = open(fileName)
    gcData = csv.reader(gcFile)
    # show all the rows in the file
    data = []
    for i, row in enumerate(gcData):
        print('{}- '.format(i+1), end='')
        print(row)
        data.append(row)
    return data

def ActivitiesNames(data):
    """
    Get activities' name
    :param data: data get from Google classroom
    :return: a list
    """
    # Activities' names
    nlist = []
    for i, col in enumerate(data[0]):
        if i > 2:
            nlist.append(col)
    return nlist

def OriPowerSchoolData():
    """
    Read Power School Template
    :return: Power School format as a list
    """
    # Power School Template
    psFile = open('PowerSchool Template.csv')
    psData = csv.reader(psFile)
    data2 = []
    for i, row in enumerate(psData):
        print('{}- '.format(i+1), end='')
        print(row)
        data2.append(row)
    print(data2)
    psFile.close()
    return data2

def UpdatePowerSchool(Data1,data):
    """
    Create and update all PowerSchool Files
    :param Data1: same as data2
    :param data: data from Google Classroom
    :return: nothing
    """
    nameList = []
    original = open('PowerSchool Template.csv','r')
    reader = csv.reader(original)
    for c in range(len(Data1)-9):
        nameList.append(Data1[9+c][1])
    print(nameList)
    nlist = ActivitiesNames(data)

    for i in range (len(nlist)):
        original = open('PowerSchool Template.csv','r')
        reader = csv.reader(original)
        name = "PowerSchool " + nlist[i] + "_pst.csv"
        copy = open(name,'w')
        writer = csv.writer(copy, delimiter = ",")
        for row in reader:

            tmp = data[1][3+i]
            dt = datetime.datetime.strptime(tmp,'%d-%b-%y')
            ndt = datetime.datetime.strftime(dt.date(),'%c')

            Data1[2][1] = data[0][3+i]
            Data1[3][1] = ndt
            for b in range(len(Data1)-9):
                for a in range(len(Data1)-9):
                    if data[3+b][0] in nameList[a]:
                        Data1[b+9][2] = int(data[3][3+i])/10.0

        original.close()
        for L in Data1:
            writer.writerow(L)
        copy.close()
