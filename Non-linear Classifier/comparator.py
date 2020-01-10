import Classifier_V5
import extractData

values = extractData.readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
#trainingValues = values[0:7530]
testValues = values[7531:15060]
getActual = extractData.makeTestSet(testValues)
#set the appropriate value for evaluator to use either test or training values
evaluator = testValues

def valCompare():
    """
    Mandate: compare values to determine accuracy
    Author: Karan Polobotu
    Date: Friday October 4th, 2019
    :return: the accuracy, number of correctly and incorectly classified values
    """
    #obtain the list of income classes from methods in the Classifier_V5
    predictedData = Classifier_V5.main(evaluator)
    actualData = Classifier_V5.realval(evaluator)
    t, f = 0, 0
    #for every predicted value that is correct, add one to t
    for i in range(len(actualData)):
        if predictedData[i] == actualData[i]:
            t += 1
        #for every incorrect predicted value, add one to f
        elif predictedData[i] != actualData[i]:
            f += 1

        i += 1
        #calculate and return the correct percentage of right values
    sum = t + f
    accuracy = float(t) / float(sum)
    finalList = [accuracy * 100, t, f]
    return finalList


if __name__ == "__main__":
    #print the results for your accuracy

    print("Reading the data")
    print("Making and training and test files")
    print("Building Classifier")
    print("Classifying test data")
    print("Classified " + str(valCompare()[1]) + " values correctly")
    print("Classified " + str(valCompare()[2]) + " values incorrectly")
    print("Accuracy: ", valCompare()[0])

