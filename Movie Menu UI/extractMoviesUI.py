from extractMovieFeatures import *

def login():


    print("WELCOME TO THE STREAMING SERVICE")
    #yes I simulated login, I do apologize
    user = input("Enter Username (testUser): ")
    Pass = input("Enter Password (CISC121): ")
    verifier = ["testUser", "CISC121"]
    verify = False
    #user inputs thier login info
    if user == verifier[0] and Pass == verifier[1]:
        verify = True
        return verify
    else:
        return verify
        

    #login verification
    #return True or False

def mainMenu(verify):

    #if credentials from login prove to be incorrect, state they are incorrect and try again
    if verify == False:
        print("access denied, your credentials are invalid")
        return mainMenu(login())
    else:
        #if credentials hold, they are true 
        print("welcome to the main menu \n type a number to access a particular feature in accordance with the following numbers: ")
        print("search - 1 \nHighly rated movies - 2 \nShortest, longest and average length movies - 3 \nreccomendations - 4 \nsave and exit - 5 \n")
        #list of commands for user to access particular functions
        try:
            command = int(input("Enter a command: "))
            end = False
            while end == False:
                if command == 1:
                    print(searchbar(listOfMovies))
                    print("\n")
                    command = int(input("Welcome to the main menu! Enter a command (6 for list of commands): "))
         
                elif command == 2:
                    print(topTen(listOfMovies))
                    print("\n")
                    command = int(input("Welcome to the main menu! Enter a command (6 for list of commands): "))
                    
                elif command == 3:
                    print(showTimeLength(listOfMovies))
                    print("\n")
                    command = int(input("Welcome to the main menu! Enter a command (6 for list of commands): "))
                    
                elif command == 4:
                    print(reccomendations())
                    print("\n")
                    command = int(input("Welcome to the main menu! Enter a command (6 for list of commands): "))

                elif command == 5:
                    end = True

                elif command == 6:
                    print("search - 1 \nHighly rated movies - 2 \nShortest, longest and average length movies - 3 \nreccomendations - 4 \nsave and exit - 5 \n")
                    print("\n")
                    command = int(input("Welcome to the main menu! Enter a command (6 for list of commands): "))
                    

            return "Goodbye!"
        except:
            ValueError
            return "there was an error with the value entered. Please restart the program and try again :("



    
if __name__ == '__main__':
    # unit test that runs all the functions in this module
    canConfirm = login()
    print(mainMenu(canConfirm))
    
