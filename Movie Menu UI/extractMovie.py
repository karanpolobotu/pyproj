"""
This module is used to read the movieData.txt information and compile
it based on the individual attrubutes required for further programming
"""



def dataExtractor (inpFile):
    #extractor takes the data from the txt file and processes it 
    movieData = list()
    with open(inpFile) as f1:
        for line in f1:
            row = line.split(",")
            movieData.append(row)
        del(movieData[0])
        return movieData

"""
This module is used to take all the data values from the txt file and organize them
based on category
"""

def dataAttributor(movieListData):
    #classify the data and place it in a dictionary which is subsequently added to a list.
    
    movies = []

    #determine genre list
    for i in range(len(movieListData)):
        detGenre = ["Action", "Adventure","Animation","Biography",
                    "Comedy","Documentary","Drama","Family","Fantasy",
                    "History","Horror","Musical","Mystery","RealityTV",
                    "Romance","SciFi","Thriller","War","Western"
            ]
        realGenre = []
        for j in range(4, 22, 1):
            if movieListData[i][j] == "1":
                realGenre.append(detGenre[j - 4])
        
        myDict = {
            "title" : movieListData[i][0],
            "rating" : float(movieListData[i][1]),
            "duration" : float(movieListData[i][2]),
            "year" : movieListData[i][3],
            #add genre
            "genre" : realGenre
            }
        #set new dictionary to hold 'Action': movieDataList[i][4] == 1, etc.
        #in doing this, we can ensure we return the correct genre values without complication
        #append the dictionary

        movies.append(myDict)

    return movies
        
"""
new method to act as searchbar to search the list of available movies. 
"""
def searchbar(movieList):
    #searchbar that works!
    searchResults = []
    searchDes = []
    x = input("Would you like to search for a movie? (Y/N): ")
    if x == "Y":
        y = input("What would you like to search?: ")
        for i in range(len(movieList)):
            if y in (movieList[i]["title"]):
                searchResults.append(movieList[i]["title"])
                i += 1
            else:
                i += 1
            
        for i in range(len(searchResults)):
            print(str(searchResults[i]) + "\n")
            
        
    
        movieSelect = input("Input which movie you would like to view details on: ")

        for i in range(len(movieList)):
            if movieSelect in (movieList[i]["title"]):
                searchDes = [movieList[i]["rating"], movieList[i]["duration"], movieList[i]["year"], movieList[i]["genre"]]
                i += 1
            else:
                i += 1
        
        

        return searchDes
            
    elif x == "N":
        exit()
    else:
        return "error"


"""
Purpose of this module is to return the movies with the top 10 ratings
"""
def topTen(movieList):
    #display top 10 ratings
    x = input("Would you like to display the top 10 rated movies? (Y/N): ")
    if x == "Y":
        #application of bubblesort algorithm
        for i in range(len(movieList)):
            for j in range(1, len(movieList)):
                if (movieList[j - 1]["rating"]) > (movieList[j]["rating"]):
                    movieList[j]["rating"], movieList[j - 1]["rating"] = movieList[j - 1]["rating"], movieList[j]["rating"]
                    j += 1
                else:
                    j += 1
            i += 1
            

        newList = [[movieList[-1]["title"], movieList[-1]["rating"]], [movieList[-2]["title"] , movieList[-2]["rating"]],
        [movieList[-3]["title"] , movieList[-3]["rating"]], [movieList[-4]["title"] , movieList[-4]["rating"]],
                    [movieList[-5]["title"] , movieList[-5]["rating"]],[movieList[-6]["title"] , movieList[-6]["rating"]],
                    [movieList[-7]["title"] , movieList[-7]["rating"]],[movieList[-8]["title"] , movieList[-8]["rating"]],
                    [movieList[-9]["title"] , movieList[-9]["rating"]],[movieList[-10]["title"] , movieList[-10]["rating"]]]


        return "Here are the top 10 movies by rating: " + str(newList)
                    
    else:
        return "ok, goodbye"

def showTimeLength(movieList):
    x = input("Would you like to view the shortest, medium and longest movies? (Y/N): ")
    if x == "Y":
        for i in range(len(movieList)):
            for j in range(1, len(movieList)):
                if (movieList[j - 1]["duration"]) > (movieList[j]["duration"]):
                    movieList[j]["duration"], movieList[j - 1]["duration"] = movieList[j - 1]["duration"], movieList[j]["duration"]
                    j += 1
                else:
                    j += 1
            i += 1

        movieLength = [movieList[0]["title"], movieList[0]["duration"]], [movieList[len(movieList)//2]["title"], movieList[len(movieList)//2]["duration"]], [movieList[len(movieList) - 1]["title"], movieList[len(movieList) - 1]["duration"]]
        return "Here are the shortest, average and longest length of movies by title: " + str(movieLength)
    else:
        pass
        
    

if __name__ == '__main__':
    inputFile = "movieData.txt"
    #testing
    movie = dataExtractor (inputFile)
    listOfMovies = dataAttributor(movie)
    #searchbar(listOfMovies)
    #topTen(listOfMovies)
    print(showTimeLength(listOfMovies))
    
