import extractData
import math

#first version of the classifier

values = extractData.readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
trainingValues = extractData.makeTrainingSet(values)
#get the training values from extractData and the website

def classSeperator():
    """
    Mandate: separate training values from above and below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: society, dictionary of below and above 50k values
    """
    #seperates values based on class
    society = {}
    upperClass, lowerClass = [], []
    j = 0
    #uses for loop to cycle through values
    while j != (len(trainingValues)):
        if trainingValues[j]['class'] == '<=50K':
            lowerClass.append(trainingValues[j])
            #seperate values to the lower and upper classes
            j += 1
        elif trainingValues[j]['class'] == '>50K':
            upperClass.append(trainingValues[j])
            j += 1
    society['lowClass'] = lowerClass
    society['highClass'] = upperClass
    return society

def lowerSeperator():
    """
    Mandate: for the below 50k, break it down into characteristics and store them into lists
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: return categorical and numerical values in different lits
    """
    #seperate below50K values into numerical and categorical
    value = classSeperator()['lowClass']
    lownumerical = {}
    #appending these values into massive lists to hold
    lowcapLoss, lowcapGain, lowhours, lowage, loweduNum = [], [], [], [], []
    lowcategorical = {}
    lowrace, lowocc, lowwork, lowmarital, lowrelationship, lowsex = [], [], [], [], [], []
    for i in range(len(value)):
        lowrace.append(value[i]['race'])
        lowocc.append(value[i]['occupation'])
        lowwork.append(value[i]['workclass'])
        lowmarital.append(value[i]['marital'])
        lowrelationship.append(value[i]['relationship'])
        lowsex.append(value[i]['sex'])

        # seperate numerical and categorical values
        lowcapLoss.append(value[i]['capitalloss'])
        loweduNum.append(value[i]['educationnum'])
        lowcapGain.append(value[i]['capitalgain'])
        lowhours.append(value[i]['hours'])
        lowage.append(value[i]['age'])
        i += 1

    lownumerical['capitalloss'] = lowcapLoss
    lownumerical['educationnum'] = loweduNum
    lownumerical['capitalgain'] = lowcapGain
    lownumerical['hours'] = lowhours
    lownumerical['age'] = lowage
    #lower class numerical values

    lowcategorical['race'] = lowrace
    lowcategorical['occupation'] = lowocc
    lowcategorical['workclass'] = lowwork
    lowcategorical['marital'] = lowmarital
    lowcategorical['relationship'] = lowrelationship
    lowcategorical['sex'] = lowsex
    #lower categorical values

    lowerAssembly = [lowcategorical, lownumerical]

    return lowerAssembly
    #figure out how to access variable in other method




def higherSeperator():
    """
    Mandate: does the same thing the lowerseperator()
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: dictionary to hold categorical and numerical values
    """
    #seperate higher classes based on numerical and categorical
    value = classSeperator()['highClass']
    highnumerical = {}
    highcapLoss, highcapGain, highhours, highage, higheduNum = [], [], [], [], []
    highcategorical = {}
    highrace, highocc, highwork, highmarital, highrelationship, highsex = [], [], [], [], [], []
    for i in range(len(value)):
        highrace.append(value[i]['race'])
        highocc.append(value[i]['occupation'])
        highwork.append(value[i]['workclass'])
        highmarital.append(value[i]['marital'])
        highrelationship.append(value[i]['relationship'])
        highsex.append(value[i]['sex'])

        # seperate numerical and categorical values
        highcapLoss.append(value[i]['capitalloss'])
        higheduNum.append(value[i]['educationnum'])
        highcapGain.append(value[i]['capitalgain'])
        highhours.append(value[i]['hours'])
        highage.append(value[i]['age'])
        i += 1

    highnumerical['capitalloss'] = highcapLoss
    highnumerical['educationnum'] = higheduNum
    highnumerical['capitalgain'] = highcapGain
    highnumerical['hours'] = highhours
    highnumerical['age'] = highage
    #append it to another dictionary to keep the numerical and categorical values above 50k

    highcategorical['race'] = highrace
    highcategorical['occupation'] = highocc
    highcategorical['workclass'] = highwork
    highcategorical['marital'] = highmarital
    highcategorical['relationship'] = highrelationship
    highcategorical['sex'] = highsex

    higherAssembly = [highcategorical, highnumerical]
    return higherAssembly


def averageDeal():
    """
    Mandate: returns averages of the class value
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: list holding average values
    """
    #get the average/comparative values we need to compare

    #GETTING AVERAGE UPPER CLASS VALUES
    highvalCapLoss = higherSeperator()[1]['capitalloss']
    highvalCapGain = higherSeperator()[1]['capitalgain']
    highvalhours = higherSeperator()[1]['hours']
    highvalage = higherSeperator()[1]['age']
    highvaleduNum = higherSeperator()[1]['educationnum']

    avgHighCapLoss = sum(highvalCapLoss)//len(highvalCapLoss)
    avgHighCapGain = sum(highvalCapGain)//len(highvalCapGain)
    avgHighHours = sum(highvalhours)//len(highvalhours)
    avgHighAge = sum(highvalage)//len(highvalage)
    avgHighEdu = sum(highvaleduNum)//len(highvaleduNum)


    #GETTING LOWER AVERAGE VALUES
    lowvalCapLoss = lowerSeperator()[1]['capitalloss']
    lowvalCapGain = lowerSeperator()[1]['capitalgain']
    lowvalhours = lowerSeperator()[1]['hours']
    lowvalage = lowerSeperator()[1]['age']
    lowvaleduNum = lowerSeperator()[1]['educationnum']

    avglowCapLoss = sum(lowvalCapLoss) // len(lowvalCapLoss)
    avglowCapGain = sum(lowvalCapGain) // len(lowvalCapGain)
    avglowHours = sum(highvalhours) // len(lowvalhours)
    avglowAge = sum(highvalage) // len(lowvalage)
    avglowEdu = sum(highvaleduNum) // len(lowvaleduNum)

    #COMBINE LISTS TO GET AVERAGES, average of below, above and midde values

    averageHigh = [avgHighCapLoss, avgHighCapGain, avgHighHours, avgHighAge, avgHighEdu]

    averageLow = [avglowCapLoss, avglowCapGain, avglowHours, avglowAge, avglowEdu]

    mid = [(avgHighCapLoss + avglowCapLoss)//2, (avgHighCapGain + avglowCapGain)//2, (avgHighHours + avglowHours)//2, (avgHighAge + avglowAge)//2, (avgHighEdu + avglowEdu)//2]

    averageDict = {'High': averageHigh, 'Low': averageLow, 'mid': mid}

    return averageDict


def raceClassifier():
    """
    Mandate: classifies and determines percentage races making above and below 50k, and uses that to determine if a race makes above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: dictionary of races above and below 50k
    """
    #get a probability result from the number of different
    Uppervalues = higherSeperator()[0]
    lowervalues = lowerSeperator()[0]
    AsianPacIslander1, AmerIndianEskimo1, Other1, Black1, White1 = 0, 0, 0, 0, 0
    for i in range (len(Uppervalues["race"])):
        if Uppervalues["race"][i] == "Black":
            Black1 += 1
        elif Uppervalues["race"][i] == "White":
            White1 += 1
        elif Uppervalues["race"][i] == "Amer-Indian-Eskimo":
            AmerIndianEskimo1 += 1
        elif Uppervalues["race"][i] == "Asian-Pac-Islander":
            AsianPacIslander1 += 1
        elif Uppervalues["race"][i] == "Other":
            Other1 += 1

        i += 1


    newSum = float(Black1 + White1 + AmerIndianEskimo1 + AsianPacIslander1 + Other1)

    percentageAsian = float(AsianPacIslander1)/newSum
    percentageAmer = float(AmerIndianEskimo1)/newSum
    percentageWhite = float(White1)/newSum
    percentageBlack = float(Black1)/newSum
    percentageOther = float(Other1)/newSum


    AsianPacIslander2, AmerIndianEskimo2, Other2, Black2, White2 = 0, 0, 0, 0, 0
    for i in range(len(lowervalues["race"])):
        if lowervalues["race"][i] == "Black":
            Black2 += 1
        elif lowervalues["race"][i] == "White":
            White2 += 1
        elif lowervalues["race"][i] == "Amer-Indian-Eskimo":
            AmerIndianEskimo2 += 1
        elif lowervalues["race"][i] == "Asian-Pac-Islander":
            AsianPacIslander2 += 1
        elif lowervalues["race"][i] == "Other":
            Other2 += 1

        i += 1

    newSum2 = float(Black2 + White2 + AmerIndianEskimo2 + AsianPacIslander2 + Other2)

    percentageAsian2 = float(AsianPacIslander2) / newSum2
    percentageAmer2 = float(AmerIndianEskimo2) / newSum2
    percentageWhite2 = float(White2) / newSum2
    percentageBlack2 = float(Black2) / newSum2
    percentageOther2 = float(Other2) / newSum2

    return percentageAsian, percentageAsian2, percentageAmer, percentageAmer2, percentageWhite, percentageWhite2,  percentageBlack, percentageBlack2, percentageOther, percentageOther2
    #Highest Ratios: above50k; Asian, White
    #Lowest Ratios: below50k; Amer, Black, Other


def occupationClassifier():
    """
    Mandate: classfies occupations and determines if specific occupations are above or below 50k
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: dictionary holding occupations above and below 50k in percentages
    """
    # get the ratio of people in specific occupations making above and below 50k, and take the higher of the two as the default
    Uppervalues = higherSeperator()[0]
    lowervalues = lowerSeperator()[0]
    occ1, occ2, occ3, occ4, occ5, occ6, occ7, occ8, occ9, occ10, occ11, occ12, occ13, occ14 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    #occupations
    for i in range(len(Uppervalues["occupation"])):
        if Uppervalues["occupation"][i] == "Tech-support":
            occ1 += 1

        elif Uppervalues["occupation"][i] == "Craft-repair":
            occ2 += 1

        elif Uppervalues["occupation"][i] == "Other-service":
            occ3 += 1

        elif Uppervalues["occupation"][i] == "Sales":
            occ4 += 1

        elif Uppervalues["occupation"][i] == "Exec-managerial":
            occ5 += 1

        elif Uppervalues["occupation"][i] == "Prof-specialty":
            occ6 += 1

        elif Uppervalues["occupation"][i] == "Handlers-cleaners":
            occ7 += 1

        elif Uppervalues["occupation"][i] == "Machine-op-inspct":
            occ8 += 1

        elif Uppervalues["occupation"][i] == "Adm-clerical":
            occ9 += 1

        elif Uppervalues["occupation"][i] == 'Farming-fishing':
            occ10 += 1

        elif Uppervalues["occupation"][i] == "Transport-moving":
            occ11 += 1

        elif Uppervalues["occupation"][i] == "Priv-house-serv":
            occ12 += 1

        elif Uppervalues["occupation"][i] == "Protective-serv":
            occ13 += 1

        elif Uppervalues["occupation"][i] == "Armed-Forces":
            occ14 += 1

        i += 1

    newSum = float(occ1 + occ2 + occ3 + occ4 + occ5 + occ6 + occ7 + occ8 + occ9 + occ10 + occ11 + occ12 + occ13 + occ14)
    #return the percentages of each occupation below and above 50k, and compare them. Take the higher one and run with it

    percentageJ1 = float(occ1) / newSum
    percentageJ2 = float(occ2) / newSum
    percentageJ3 = float(occ3) / newSum
    percentageJ4 = float(occ4) / newSum
    percentageJ5 = float(occ5) / newSum
    percentageJ6 = float(occ6) / newSum
    percentageJ7 = float(occ7) / newSum
    percentageJ8 = float(occ8) / newSum
    percentageJ9 = float(occ9) / newSum
    percentageJ10 = float(occ10) / newSum
    percentageJ11 = float(occ11) / newSum
    percentageJ12 = float(occ12) / newSum
    percentageJ13 = float(occ13) / newSum
    percentageJ14 = float(occ14) / newSum

    occ21, occ22, occ23, occ24, occ25, occ26, occ27, occ28, occ29, occ210, occ211, occ212, occ213, occ214 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(len(lowervalues["occupation"])):
        if lowervalues["occupation"][i] == "Tech-support":
            occ21 += 1

        elif lowervalues["occupation"][i] == "Craft-repair":
            occ22 += 1

        elif lowervalues["occupation"][i] == "Other-service":
            occ23 += 1

        elif lowervalues["occupation"][i] == "Sales":
            occ24 += 1

        elif lowervalues["occupation"][i] == "Exec-managerial":
            occ25 += 1

        elif lowervalues["occupation"][i] == "Prof-specialty":
            occ26 += 1

        elif lowervalues["occupation"][i] == "Handlers-cleaners":
            occ27 += 1

        elif lowervalues["occupation"][i] == "Machine-op-inspct":
            occ28 += 1

        elif lowervalues["occupation"][i] == "Adm-clerical":
            occ29 += 1

        elif lowervalues["occupation"][i] == 'Farming-fishing':
            occ210 += 1

        elif lowervalues["occupation"][i] == "Transport-moving":
            occ211 += 1

        elif lowervalues["occupation"][i] == "Priv-house-serv":
            occ212 += 1

        elif lowervalues["occupation"][i] == "Protective-serv":
            occ213 += 1

        elif lowervalues["occupation"][i] == "Armed-Forces":
            occ214 += 1

        i += 1

    newSum = float(occ21 + occ22 + occ23 + occ24 + occ25 + occ26 + occ27 + occ28 + occ29 + occ210 + occ211 + occ212 + occ213 + occ214)

    percentage2J1 = float(occ21) / newSum
    percentage2J2 = float(occ22) / newSum
    percentage2J3 = float(occ23) / newSum
    percentage2J4 = float(occ24) / newSum
    percentage2J5 = float(occ25) / newSum
    percentage2J6 = float(occ26) / newSum
    percentage2J7 = float(occ27) / newSum
    percentage2J8 = float(occ28) / newSum
    percentage2J9 = float(occ29) / newSum
    percentage2J10 = float(occ210) / newSum
    percentage2J11 = float(occ211) / newSum
    percentage2J12 = float(occ212) / newSum
    percentage2J13 = float(occ213) / newSum
    percentage2J14 = float(occ214) / newSum

    fiftyK = {}
    #add to a dictionary to give us the higher percentage

    if percentageJ1 < percentage2J1:
        fiftyK["above50K 2J1"] = percentage2J1
    else:
        fiftyK["below50K 2J1"] = percentage2J1

    if percentageJ2 < percentage2J2:
        fiftyK["above50K 2J2"] = percentage2J2
    else:
        fiftyK["below50K 2J2"] = percentage2J2

    if percentageJ3 < percentage2J3:
        fiftyK["above50K 2J3"] = percentage2J3
    else:
        fiftyK["below50K 2J3"] = percentage2J3

    if percentageJ4 < percentage2J4:
        fiftyK["above50K 2J4"] = percentage2J4
    else:
        fiftyK["below50K 2J4"] = percentage2J4

    if percentageJ5 < percentage2J5:
        fiftyK["above50K 2J5"] = percentage2J5
    else:
        fiftyK["below50K 2J5"] = percentage2J5

    if percentageJ6 < percentage2J6:
        fiftyK["above50K 2J6"] = percentage2J6
    else:
        fiftyK["below50K 2J6"] = percentage2J6

    if percentageJ7 < percentage2J7:
        fiftyK["above50K 2J7"] = percentage2J7
    else:
        fiftyK["below50K 2J7"] = percentage2J7

    if percentageJ8 < percentage2J8:
        fiftyK["above50K 2J8"] = percentage2J8
    else:
        fiftyK["below50K 2J8"] = percentage2J8

    if percentageJ9 < percentage2J9:
        fiftyK["above50K 2J9"] = percentage2J9
    else:
        fiftyK["below50K 2J9"] = percentage2J9

    if percentageJ10 < percentage2J10:
        fiftyK["above50K 2J10"] = percentage2J10
    else:
        fiftyK["below50K 2J10"] = percentage2J10

    if percentageJ11 < percentage2J11:
        fiftyK["above50K 2J11"] = percentage2J11
    else:
        fiftyK["below50K 2J11"] = percentage2J11

    if percentageJ12 < percentage2J12:
        fiftyK["above50K 2J12"] = percentage2J12
    else:
        fiftyK["below50K 2J12"] = percentage2J12

    if percentageJ13 < percentage2J13:
        fiftyK["above50K 2J13"] = percentage2J13
    else:
        fiftyK["below50K 2J13"] = percentage2J13

    if percentageJ14 < percentage2J14:
        fiftyK["above50K 2J14"] = percentage2J14
    else:
        fiftyK["below50K 2J14"] = percentage2J14

    return fiftyK
    #all results came out below 50k, therefore simply return False

def maritalClassifier():
    """
    Mandate: classifies marital values
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: list of the marital positions above and below 50k
    """
    #same as occupational classifier for marriage
    Uppervalues = higherSeperator()[0]
    lowervalues = lowerSeperator()[0]
    mar1, mar2, mar3, mar4, mar5, mar6, mar7 = 0, 0, 0, 0, 0, 0, 0
    for i in range(len(Uppervalues["marital"])):
        if Uppervalues["marital"][i] == "Married-civ-spouse":
            mar1 += 1

        elif Uppervalues["marital"][i] == "Divorced":
            mar2 += 1

        elif Uppervalues["marital"][i] == "Never-married":
            mar3 += 1

        elif Uppervalues["marital"][i] == "Separated":
            mar4 += 1

        elif Uppervalues["marital"][i] == "Widowed":
            mar5 += 1

        elif Uppervalues["marital"][i] == "Married-spouse-absent":
            mar6 += 1

        elif Uppervalues["marital"][i] == "Married-AF-spouse":
            mar7 += 1

        i += 1

    newSum = float(mar1 + mar2 + mar3 + mar4 + mar5 + mar6 + mar7)

    marJ1 = float(mar1) / newSum
    marJ2 = float(mar2) / newSum
    marJ3 = float(mar3) / newSum
    marJ4 = float(mar4) / newSum
    marJ5 = float(mar5) / newSum
    marJ6 = float(mar6) / newSum
    marJ7 = float(mar7) / newSum


    mar21, mar22, mar23, mar24, mar25, mar26, mar27 = 0, 0, 0, 0, 0, 0, 0
    for i in range(len(lowervalues["marital"])):
        if lowervalues["marital"][i] == "Married-civ-spouse":
            mar21 += 1

        elif lowervalues["marital"][i] == "Divorced":
            mar22 += 1

        elif lowervalues["marital"][i] == "Never-married":
            mar23 += 1

        elif lowervalues["marital"][i] == "Separated":
            mar24 += 1

        elif lowervalues["marital"][i] == "Widowed":
            mar25 += 1

        elif lowervalues["marital"][i] == "Married-spouse-absent":
            mar26 += 1

        elif lowervalues["marital"][i] == "Married-AF-spouse":
            mar27 += 1


        i += 1

    newSum = float(
        mar21 + mar22 + mar23 + mar24 + mar25 + mar26 + mar27 )

    mar2J1 = float(mar21) / newSum
    mar2J2 = float(mar22) / newSum
    mar2J3 = float(mar23) / newSum
    mar2J4 = float(mar24) / newSum
    mar2J5 = float(mar25) / newSum
    mar2J6 = float(mar26) / newSum
    mar2J7 = float(mar27) / newSum

    fiftyK = {}

    if marJ1 < mar2J1:
        fiftyK["above50K 2J1"] = mar2J1
    else:
        fiftyK["below50K 2J1"] = mar2J1

    if marJ2 < mar2J2:
        fiftyK["above50K 2J2"] = mar2J2
    else:
        fiftyK["below50K 2J2"] = mar2J2

    if marJ3 < mar2J3:
        fiftyK["above50K 2J3"] = mar2J3
    else:
        fiftyK["below50K 2J3"] = mar2J3

    if marJ4 < mar2J4:
        fiftyK["above50K 2J4"] = mar2J4
    else:
        fiftyK["below50K 2J4"] = mar2J4

    if marJ5 < mar2J5:
        fiftyK["above50K 2J5"] = mar2J5
    else:
        fiftyK["below50K 2J5"] = mar2J5

    if marJ6 < mar2J6:
        fiftyK["above50K 2J6"] = mar2J6
    else:
        fiftyK["below50K 2J6"] = mar2J6

    if marJ7 < mar2J7:
        fiftyK["above50K 2J7"] = mar2J7
    else:
        fiftyK["below50K 2J7"] = mar2J7



    return fiftyK

def relationshipClassifier():
    """
    Mandate: classifies relationship values
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: list of the relationship positions above and below 50k
    """
    #same as marital and occupational, exclusive to relationship
    Uppervalues = higherSeperator()[0]
    lowervalues = lowerSeperator()[0]
    mar1, mar2, mar3, mar4, mar5, mar6 = 0, 0, 0, 0, 0, 0
    for i in range(len(Uppervalues["marital"])):
        if Uppervalues["relationship"][i] == "Wife":
            mar1 += 1

        elif Uppervalues["relationship"][i] == "Own-child":
            mar2 += 1

        elif Uppervalues["relationship"][i] == "Husband":
            mar3 += 1

        elif Uppervalues["relationship"][i] == "Not-in-family":
            mar4 += 1

        elif Uppervalues["relationship"][i] == "Other-relativ":
            mar5 += 1

        elif Uppervalues["relationship"][i] == "Unmarried":
            mar6 += 1

        i += 1

    newSum = float(mar1 + mar2 + mar3 + mar4 + mar5 + mar6)

    marJ1 = float(mar1) / newSum
    marJ2 = float(mar2) / newSum
    marJ3 = float(mar3) / newSum
    marJ4 = float(mar4) / newSum
    marJ5 = float(mar5) / newSum
    marJ6 = float(mar6) / newSum

    mar21, mar22, mar23, mar24, mar25, mar26 = 0, 0, 0, 0, 0, 0
    for i in range(len(lowervalues["relationship"])):
        if lowervalues["relationship"][i] == "Wife":
            mar21 += 1

        elif lowervalues["relationship"][i] == "Divorced":
            mar22 += 1

        elif lowervalues["relationship"][i] == "Own-child":
            mar23 += 1

        elif lowervalues["relationship"][i] == "Not-in-family":
            mar24 += 1

        elif lowervalues["relationship"][i] == "Other-relativ":
            mar25 += 1

        elif lowervalues["relationship"][i] == "Unmarried":
            mar26 += 1


        i += 1

    newSum = float(
        mar21 + mar22 + mar23 + mar24 + mar25 + mar26)

    mar2J1 = float(mar21) / newSum
    mar2J2 = float(mar22) / newSum
    mar2J3 = float(mar23) / newSum
    mar2J4 = float(mar24) / newSum
    mar2J5 = float(mar25) / newSum
    mar2J6 = float(mar26) / newSum

    fiftyK = {}

    if marJ1 < mar2J1:
        fiftyK["above50K 2J1"] = mar2J1
    else:
        fiftyK["below50K 2J1"] = mar2J1

    if marJ2 < mar2J2:
        fiftyK["above50K 2J2"] = mar2J2
    else:
        fiftyK["below50K 2J2"] = mar2J2

    if marJ3 < mar2J3:
        fiftyK["above50K 2J3"] = mar2J3
    else:
        fiftyK["below50K 2J3"] = mar2J3

    if marJ4 < mar2J4:
        fiftyK["above50K 2J4"] = mar2J4
    else:
        fiftyK["below50K 2J4"] = mar2J4

    if marJ5 < mar2J5:
        fiftyK["above50K 2J5"] = mar2J5
    else:
        fiftyK["below50K 2J5"] = mar2J5

    if marJ6 < mar2J6:
        fiftyK["above50K 2J6"] = mar2J6
    else:
        fiftyK["below50K 2J6"] = mar2J6


    return fiftyK


def sexClassifier():
    """
    Mandate: classifies gender values
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: list of the genders above and below 50k
    """
    #classifies the gender, same as occupational
    Uppervalues = higherSeperator()[0]
    lowervalues = lowerSeperator()[0]
    mar1, mar2= 0, 0
    for i in range(len(Uppervalues["sex"])):
        if Uppervalues["sex"][i] == "Male":
            mar1 += 1

        elif Uppervalues["sex"][i] == "Femaile":
            mar2 += 1


        i += 1

    newSum = float(mar1 + mar2)

    marJ1 = float(mar1) / newSum
    marJ2 = float(mar2) / newSum

    mar21, mar22, mar23, mar24, mar25, mar26, mar27, mar28 = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(len(lowervalues["sex"])):
        if lowervalues["sex"][i] == "Male":
            mar21 += 1

        elif lowervalues["sex"][i] == "Female":
            mar22 += 1



        i += 1

    newSum = float(mar21 + mar22)

    mar2J1 = float(mar21) / newSum
    mar2J2 = float(mar22) / newSum


    fiftyK = {}

    if marJ1 < mar2J1:
        fiftyK["above50K 2J1"] = mar2J1
    else:
        fiftyK["below50K 2J1"] = mar2J1

    if marJ2 < mar2J2:
        fiftyK["above50K 2J2"] = mar2J2
    else:
        fiftyK["below50K 2J2"] = mar2J2

    return fiftyK


def workClassClassifier():
    """
    Mandate: classifies workclass values
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: list of the work class positions above and below 50k
    """
    #classifies workclass, same as sex
    Uppervalues = higherSeperator()[0]
    lowervalues = lowerSeperator()[0]
    mar1, mar2, mar3, mar4, mar5, mar6, mar7, mar8 = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(len(Uppervalues["workclass"])):
        if Uppervalues["workclass"][i] == "Private":
            mar1 += 1

        elif Uppervalues["workclass"][i] == "Self-emp-not-inc":
            mar2 += 1

        elif Uppervalues["workclass"][i] == "Self-emp-inc":
            mar3 += 1

        elif Uppervalues["workclass"][i] == "Federal-gov":
            mar4 += 1

        elif Uppervalues["workclass"][i] == "Local-gov":
            mar5 += 1

        elif Uppervalues["workclass"][i] == "State-gov":
            mar6 += 1

        elif Uppervalues["workclass"][i] == "Without-pay":
            mar7 += 1

        elif Uppervalues["workclass"][i] == "Never-worked":
            mar8 += 1

        i += 1

    newSum = float(mar1 + mar2 + mar3 + mar4 + mar5 + mar6 + mar7 + mar8)

    marJ1 = float(mar1) / newSum
    marJ2 = float(mar2) / newSum
    marJ3 = float(mar3) / newSum
    marJ4 = float(mar4) / newSum
    marJ5 = float(mar5) / newSum
    marJ6 = float(mar6) / newSum
    marJ7 = float(mar7) / newSum
    marJ8 = float(mar8) / newSum

    mar21, mar22, mar23, mar24, mar25, mar26, mar27, mar28 = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(len(lowervalues["workclass"])):
        if lowervalues["workclass"][i] == "Private":
            mar21 += 1

        elif lowervalues["workclass"][i] == "Self-emp-not-inc":
            mar22 += 1

        elif lowervalues["workclass"][i] == "Self-emp-inc":
            mar23 += 1

        elif lowervalues["workclass"][i] == "Federal-gov":
            mar24 += 1

        elif lowervalues["workclass"][i] == "Local-gov":
            mar25 += 1

        elif lowervalues["workclass"][i] == "State-gov":
            mar26 += 1

        elif lowervalues["workclass"][i] == "Without-pay":
            mar27 += 1

        elif lowervalues["workclass"][i] == "Never-worked":
            mar28 += 1

        i += 1

    newSum = float(mar21 + mar22 + mar23 + mar24 + mar25 + mar26 + mar27)

    mar2J1 = float(mar21) / newSum
    mar2J2 = float(mar22) / newSum
    mar2J3 = float(mar23) / newSum
    mar2J4 = float(mar24) / newSum
    mar2J5 = float(mar25) / newSum
    mar2J6 = float(mar26) / newSum
    mar2J7 = float(mar27) / newSum
    mar2J8 = float(mar28) / newSum

    fiftyK = {}

    if marJ1 < mar2J1:
        fiftyK["above50K 2J1"] = mar2J1
    else:
        fiftyK["below50K 2J1"] = mar2J1

    if marJ2 < mar2J2:
        fiftyK["above50K 2J2"] = mar2J2
    else:
        fiftyK["below50K 2J2"] = mar2J2

    if marJ3 < mar2J3:
        fiftyK["above50K 2J3"] = mar2J3
    else:
        fiftyK["below50K 2J3"] = mar2J3

    if marJ4 < mar2J4:
        fiftyK["above50K 2J4"] = mar2J4
    else:
        fiftyK["below50K 2J4"] = mar2J4

    if marJ5 < mar2J5:
        fiftyK["above50K 2J5"] = mar2J5
    else:
        fiftyK["below50K 2J5"] = mar2J5

    if marJ6 < mar2J6:
        fiftyK["above50K 2J6"] = mar2J6
    else:
        fiftyK["below50K 2J6"] = mar2J6

    if marJ7 < mar2J7:
        fiftyK["above50K 2J7"] = mar2J7
    else:
        fiftyK["below50K 2J7"] = mar2J7

    if marJ7 < mar2J7:
        fiftyK["above50K 2J7"] = mar2J7
    else:
        fiftyK["below50K 2J7"] = mar2J7

    if marJ8< mar2J8:
        fiftyK["above50K 2J8"] = mar2J8
    else:
        fiftyK["below50K 2J8"] = mar2J8


    return fiftyK
