import extractData
import Classifier_V4

values = extractData.readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
trainingValues = extractData.makeTrainingSet(values)
#^^training data used
avgDictF = Classifier_V4.averageDeal()


def numBreakdown():
    """
    Mandate: takes the average values and accesses them for comparison
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: list of the marital positions above and below 50k
    """
    #in order: avgCapLoss, avgCapGain, avgHours, avgAge, avgEdu
    bustdownA = avgDictF['High'][0], avgDictF['mid'][0], avgDictF['Low'][0]
    bustdownB = avgDictF['High'][1], avgDictF['mid'][1], avgDictF['Low'][1]
    bustdownC = avgDictF['High'][2], avgDictF['mid'][2], avgDictF['Low'][2]
    bustdownD = avgDictF['High'][3], avgDictF['mid'][3], avgDictF['Low'][3]
    bustdownE = avgDictF['High'][4], avgDictF['mid'][4], avgDictF['Low'][4]
    collection = [bustdownA[1], bustdownB[1], bustdownC[1], bustdownD[1], bustdownE[1]]
    return collection



def main(evaluator):
    """
    Mandate: classifies marital values
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: list of the marital positions above and below 50k
    :param evaluator: takes the test data we need and runs it through here
    :return: returns the data for above and belo 50k values
    """
    #run this to go through the entire list to get predicted class data
    data = []
    for i in range(len(evaluator)):
        data.append(reader(evaluator[i]))
        i += 1
    return data

def realval(record):
    """
    Mandate: extracts the class value to get actual value
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param record: takes the values from the line
    :return: returns actual income value
    """
    #get the actual class data
    realClass = []
    for i in range(len(record)):
        realClass.append(record[i]['class'])
    return realClass


def reader(record):
    """
    Mandate: returns an income prediction based on all 11 traits/factors
    :param record: take one line from the website
    :return: a prediction, <=50K, >50k
    """
    #append the true or false values
    currentClass = []
    currentClass.append(age(record['age']))
    currentClass.append(eduNum(record['educationnum']))
    currentClass.append(capitalGain(record['capitalgain']))
    currentClass.append(capitalLoss(record["capitalloss"]))
    currentClass.append(hours(record['hours']))
    currentClass.append(race(record['race']))
    currentClass.append(occupation(record['occupation']))
    currentClass.append(marital(record['marital']))
    currentClass.append(relationship(record['relationship']))
    currentClass.append(sex(record['sex']))
    currentClass.append(workClass(['workclass']))

    j, k = 0, 0
    for i in range(len(currentClass)):
        if currentClass[i] == False:
            j += 1
            i += 1

        else:
            k += 1
            i += 1

    if k > j:
        return "<=50K"
    elif k < j:
        return ">50K"

#ALL YOU NEED TO DO IS TO CHANGE TO TEST VALUES AND FIND ACCURACY, THEN MAIN



def age(age):
    """
    Mandate: determine if this is above the average age
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param age: take the age value from record
    :return: return True or False
    """
    #returns a value of True or False for the function if its above or below the mid value
    above50k = False
    breakdown = numBreakdown()
    comparator = breakdown[3]
    if age >= comparator:
        above50k = True
    else:
        above50k = True
    return above50k

def eduNum(educationNum):
    """
    Mandate: compare education number with average, determine
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param educationNum: education number from record
    :return: return True or False
    """
    #same as age for eduNum
    above50k = False
    breakdown = numBreakdown()
    comparator = breakdown[4]
    if educationNum >= comparator:
        above50k = True
    else:
        above50k = False
    return above50k

def capitalGain(capGain):
    """
    Mandate: compare capital gain and averages, determine
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param capGain: capital gain from record
    :return: return True or False
    """
    #same as age for capGain
    above50k = False
    breakdown = numBreakdown()
    comparator = breakdown[1]
    if capGain >= comparator:
        above50k = True
    else:
        above50k = False
    return above50k

def capitalLoss(capLoss):
    """
    Mandate: compare capital loss and averages, determine
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param capLoss: capital loss from record/line
    :return: True or False
    """
    #same as age for capLoss
    above50k = False
    breakdown = numBreakdown()
    comparator = breakdown[0]
    if capLoss >= comparator:
        above50k = True
    else:
        above50k = False
    return above50k

def hours(hours):
    """
    Mandate: compare hours worked and averages, determine if its above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param hours: hours from record
    :return: True or False
    """
    #same as age for hours
    above50k = False
    breakdown = numBreakdown()
    comparator = breakdown[2]
    if hours >= comparator:
        above50k = True
    else:
        above50k = False
    return above50k

def race(race):
    """
    Mandate: determines which race makes above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param race:
    :return:
    """
    #classifies based on race
    above50k = False
    if race == 'Black' or race == 'Amer' or race == 'Other':
        above50k = False
    elif race == 'White' or 'Asian-Pac-Islander':
        above50k = True

    return above50k

def occupation(occ):
    """
    Mandate: determines which occupations are above and below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param occ: occupation of record
    :return: True or False
    """
    #classifies based on occupation
    above50k = False
    if occ == 'Tech-support' or occ == 'Sales' or occ == 'Exec-managerial' or occ == "Prof-specialty" or occ == "Armed-Forces" or occ == "Protective-serv":
        above50k = False
    elif occ == 'Craft-repair' or occ == 'Other-service' or occ == "Handlers-cleaners" or occ == "Machine-op-inspct" or occ == "Adm-clerical" or occ == "Farming-fishing" or occ == "Transport-moving" or occ == "Priv-house-serv":
        above50k = True

    return above50k
def marital(marital):
    """
    Mandate: compare marital status, determine if its above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param marital: takes marital status
    :return: True or False
    """
    #classified based on marriage status
    above50K = False
    if marital == "Married-civ-spouse" or "Married-AF-spouse":
        above50K = False
    else:
        above50K = True
    return above50K
def relationship(relationship):
    """
    Mandate: compare relationship status, determine if its above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param relationship: relationship status from record
    :return: True or False
    """
    #same as marital for relationship
    above50K = False
    if relationship == "Not-in-family" or "Unmarried":
        above50K = True
    else:
        above50K = False

    return above50K

def sex(sex):
    """
    Mandate: compare gender, determine if its above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param sex: gender from record
    :return: True or False
    """
    #same as relationship
    if sex == "Female":
        above50K = True
    else:
        above50K = False

    return above50K

def workClass(workclass):
    """
    Mandate: compare workclass, determine if its above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :param workclass: workclass status
    :return: True or False
    """
    #same as sex
    above50K = False
    if workclass == "Private" or "Without-pay":
        above50K = True
    else:
        above50K = False

    return above50K

if __name__ == "__main__":
    print(none)
