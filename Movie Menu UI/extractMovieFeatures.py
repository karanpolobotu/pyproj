
def dataExtractor (inpFile):


    #extractor takes the data from the txt file and processes it 
    movieData = list()
    with open(inpFile) as f1:
        for line in f1:
            row = line.split(",")
            movieData.append(row)
        del(movieData[0])
        return movieData

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

def searchbar(movieList):       


    #searchbar that works!
    searchResults = []
    searchDes = []
    #watched list file
    x = input("Would you like to search for a movie? (Y/N): ")
    x = x.lower()
    if x == "y":
        y = input("What would you like to search?: ")
        for i in range(len(movieList)):
            if y.lower() in (movieList[i]["title"].lower()):
                searchResults.append(movieList[i]["title"])
                i += 1
            else:
                i += 1

        if len(searchResults) == 0:
            return "Nothing found!, try again"
        else: 
            for i in range(len(searchResults)):
                print(searchResults[i] + "\n")
            
        
    
        movieSelect = input("Input which movie you would like to view details on: ")
        
        for i in range(len(movieList)):
            if movieSelect.lower() in (movieList[i]["title"].lower()):
                searchDes = [movieList[i]["title"], movieList[i]["rating"], movieList[i]["duration"], movieList[i]["year"], movieList[i]["genre"]]
                break;
            else:
                i += 1

        print(searchDes)
        

        watch = input('would you like to watch this movie? (Y/N): ')
        watch = watch.lower()
        watchedFilms = []
        if watch == 'y':
            with open('watchlist.txt') as f1:
                for line in f1:
                    row = line.split(",")
                    watchedFilms.append(row)
                for i in range(len(watchedFilms)):
                    if searchDes[0] == watchedFilms[0][i]:
                        return "You've already seen this film!"
                #parse through function, delete repetitive instances of a desired watch
                    else:
                        watchlist = open("watchlist.txt", "a+")
                        
                        watchlist.write(searchDes[0])
                        watchlist.write(",")
                        watchlist.write(str(searchDes[1]))
                        watchlist.write(",")
                        watchlist.write(str(searchDes[2]))
                        watchlist.write(",")
                        watchlist.write(str(searchDes[3]))
                        watchlist.write(",")
                        watchlist.write((str(searchDes[4])) + "\n")
                        watchlist.close()
                        return "added"
            
         

        if watch == 'n':
            return "Done"
    
    elif x == 'n':
        return 0
    else:
        return "error"
    

    
            
        
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
        #main menu
        return "ok"


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
        return "Here are the shortest, average and longest length of movies by title in seconds: " + str(movieLength)
    elif x == "Quit":
        exit()
    else:
        pass
        #main menu


def reccomendations():


    x = input("Would you like movie suggestions testUser?(Y/N): ")
    
    #read txt values
    watchList = "watchlist.txt"

    def reader(watchList):
   
    
        watchData = []
        #read the watch history of the user
        with open(watchList) as f1:
            for line in f1:
                row = line.split(",")
                watchData.append(row)
            return watchData


    def search(result):
    
    
        #classify the data based on genre
        genre = []
        for j in range (len(result)):
            for i in range(4, len(result[j]), 1):
                genre.append(result[j][i])
                i += 1
            j += 1
        return genre

    def counter(genreHolder):
    
    
        #take the genre from the particualar movies, count every instance of each genre
        q, w, e, r, t, y, u, o, p, a, s, d, f, g, h, j, k, l, z = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        top = {}
        for i in range(len(genreHolder)):
            if "Action" in genreHolder[i]:
                q += 1
                i += 1
            elif "Adventure" in genreHolder[i]:
                w += 1
                i += 1
            elif "Animation" in genreHolder[i]:
                e += 1
                i += 1
            elif "Biography" in genreHolder[i]:
                r += 1
                i += 1
            elif "Comedy" in genreHolder[i]:
                t += 1
                i += 1
            elif "Documentary" in genreHolder[i]:
                y += 1
                i += 1
            elif "Drama" in genreHolder[i]:
                u += 1
                i += 1
            elif "Family" in genreHolder[i]:
                o += 1
                i += 1
            elif "Fantasy" in genreHolder[i]:
                p += 1
                i += 1
            elif "History" in genreHolder[i]:
                a += 1
                i += 1
            elif "Horror" in genreHolder[i]:
                s += 1
                i += 1
            elif "Musical" in genreHolder[i]:
                d += 1
                i += 1
            elif "Mystery" in genreHolder[i]:
                f += 1
                i += 1
            elif "RealityTV" in genreHolder[i]:
                g += 1
                i += 1
            elif "Romance" in genreHolder[i]:
                h += 1
                i += 1
            elif "SciFi" in genreHolder[i]:
                j += 1
                i += 1
            elif "Thriller" in genreHolder[i]:
                k += 1
                i += 1
            elif "War" in genreHolder[i]:
                l += 1
                i += 1
            elif "Western" in genreHolder[i]:
                z += 1
                i += 1
        top = {"Action" : q, "Adventure" : w,
               "Animation" : e,"Biography" : r,
               "Comedy" : t, "Documentary" : y,
               "Drama" : u, "Family" : o,
               "Fantasy" : p, "History" : a,
               "Horror" : s, "Musical" : d,
               "Mystery" : f, "RealityTV" : g,
              "Romance" : h,"SciFi" : j,
               "Thriller" : k, "War" : l, "Western" : z}
        inverse = [(value, key) for key, value in top.items()]
        
        #taken from stackoverflow : https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        #used to get the most watched genre 
        return max(inverse)[1], min(inverse)[1]

        

            #if a genre is in this element, counter goes up
    def reccomender(count, movieList):
    
    
        #based on the highest few counts, return the reccommended genres
        most = []
        least = []
        #sort the rating values using bubblesort, then return top 10
            
        for i in range(len(movieList)):
            for j in range(1, len(movieList)):
                if (movieList[j - 1]["rating"]) > (movieList[j]["rating"]):
                    movieList[j]["rating"], movieList[j - 1]["rating"] = movieList[j - 1]["rating"], movieList[j]["rating"]
                    j += 1
                else:
                    j += 1
            i += 1

        for i in range(len(movieList)):
            if count[0] in movieList[i]["genre"]:
                #most.append(movieList[i]["rating"])
                #if we ran this command, we would see the rakings of all movies in the drama genre ordered
                #this is nice, but not needed. Instead we need to suggest the user the title
                most.append(movieList[i]["title"])
                i += 1
        topReccomended = [most[-1], most[-2], most[-3], most[-4], most[-5], most[-6], most[-7], most[-8], most[-9], most[-10]]
                

        
        for i in range(len(movieList)):
            if count[1] in movieList[i]["genre"]:
                least.append(movieList[i]["title"])
                i += 1


        lowReccomended = [least[-1], least[-2], least[-3], least[-4], least[-5], least[-6], least[-7], least[-8], least[-9], least[-10]]
        
        
        



        
        return "Based on your watch history, you might like " + str(count[0]) + " films like: " + str(topReccomended) + "\n" + "Don't be afraid to try new things! Perhaps you might like " + str(count[1]) + " movies! Here are the top movies in that category: " + str(lowReccomended) + "\n"

        
    if x == "Y":    
        procList = reader(watchList)
        countGenre = search(procList)
        mostAndLeast = counter(countGenre)
        return reccomender(mostAndLeast, listOfMovies)
    elif x == "N":
        return None
        
inputFile = "movieData.txt"
movie = dataExtractor (inputFile)
listOfMovies = dataAttributor(movie)
#lay the groundwork for the movieData to be incorporated and used within the program

if __name__ == '__main__':
    #Unit test that tests every single function individually 
    
    
    print(searchbar(listOfMovies))
    print(topTen(listOfMovies))
    print(showTimeLength(listOfMovies))
    print(reccomendations())
    
