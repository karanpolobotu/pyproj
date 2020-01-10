"""
CREATED BY KARAN POLOBOTU
Date: Friday November 29th, 2019
"""
def split_int_pairs(ints):
    """Returns a copy of ints, a list of integers, with the value None
    inserted between any two identical values. For example:
        split_int_pairs([])
            returns []
        split_int_pairs([-5])
            returns [-5]
        split_int_pairs([-5, 1])
            returns [-5, 1]
        split_int_pairs([-5, -5])
            returns [-5, None, -5]
        split_int_pairs([0, 1, 0, 1, 1, 0, 0])
            returns [0, 1, 0, 1, None, 1, 0, None, 0]
            """

    if len(ints) <= 1:
        return ints
    #create three cases, if length is 0, 1 or 2

    if len(ints) == 2:
        if ints[0] == ints[1]:
            ints.insert(1, None)
            return ints
        if ints[0] != ints[1]:
            return ints

    else:
        holder = []
        #create a list to break every list into two value lists (2D Array)

        for i in range(len(ints) - 1):
            holdingValue = split_int_pairs([ints[i], ints[i + 1]])

            if len(holder) == 0:
                for j in (holdingValue):
                    holder.append(j)
                    #if the 2D lists have 2 element, just append it to our new list

            else:
                for k in range(1, len(holdingValue)):
                    holder.append(holdingValue[k])
                    #otherwise, compare the individual 2 element lists to our three cases, get our result, and then return it


        return holder
        #return out new list in the end


def count_split_char_pairs(s):
    """Returns an integer representing the number of occurrences of two
    identical characters being separated by one other (i.e., non-identical)
    character in string s. For example:
        count_split_char_pairs('')
            returns 0
	count_split_char_pairs('aA')
            returns 0
        count_split_char_pairs('aAa')
            returns 1
        count_split_char_pairs('bAbA')
            returns 2
        count_split_char_pairs('BcBcBc')
            returns 4 (from overlapping split pairs BcB, cBc, BcB, and cBc)
    """

    if len(s) <= 2:
        return 0

    if len(s) == 3:
        if s[0] != s[2]:
            return 0
        elif s[0] == s[2]:
            return 1
    else:
        holder = []
        #create a list to break every three values into individual lists that we can evaluate

        for i in range(len(s) - 1):
            holdingValue = count_split_char_pairs([s[i:i + 1], s[i + 1: i + 2], s[i + 2:i + 3]])
            #get a value that determines if two characters are seperated by a character or not
            holder.append(holdingValue)
            #append those values into a list

        return sum(holder)
        #return the sum of those values to tell you how many instances of a character are seperated by a character

#return out new list in the end"""

def check_nesting(s):
    """s is a str containing only square brackets, '[' and ']'. Returns True
    if s is a nesting of zero or more pairs of square brackets, and False
    otherwise. For example:
        check_nesting('')
            returns True (i.e., 0 pairs of square brackets)
        check_nesting('[')
            returns False
        check_nesting('[]')
            returns True
        check_nesting('[]]')
            returns False
        check_nesting('[[]]')
            returns True
        check_nesting('[[[[[[[[[]]]]]]]]]')
            returns True
    """
    holder = []
    counter1 = 0
    if len(s) == 0:
        return True
    elif len(s) == 1:
        return False

    elif len(s) == 2:
        if s[0] == '[' or s[0] == ']' and s[1] == '[' or s[1] == ']' :
            if s[0] == '[' and s[1] == ']':
                return True
            else:
                return s
    else:

        for i in range(len(s)):
            #create a list to hold every single character
            holdingValue = check_nesting([s[i]])
            holder.append(holdingValue)

        for j in range(len(holder)):
            #evaluate the list values to determine which if it has nesting
            if holder[j] == '[':
                counter1 += 1
            elif holder[j] == ']':
                counter1 -= 1
                #if there are an equal number of brackets to have nesting, you will get 0 otherwise you will have a negative or positive value
                #based on that, you can determine if it's true or false
            else:
                counter1 += 0

        for k in range(len(holder)):
            if s[k] == "[":
                #if you get one character, increase count1
                counter1 += 1


            elif s[k] == "]":
                #if you get another character, increase count2
                counter1 -= 1

        if counter1 == 0:
            return True
        else:
            return False



        #return out new list in the end



def find_double(ints, index=0):
    """Returns True if integer list ints contains two adjacent elements where the
    second element is twice the value of the first.
        find_double([])
            returns False
        find_double([3])
            returns False
        find_double([3, 5])
            returns False
        find_double([3, 5, 6])
            returns False (since although 3 * 2 is 6, the 6 does not immediately follow the 3)
        find_double([3, 6])
            returns True (since 3 * 2 is 6, and 3 comes before 6 in ints)
        find_double([7, 8, 16, 15, 3, 22])
            returns True (since 8 * 2 is 16, and 8 comes before 16 in ints)
        find_double([7, 8, 16, 14, 28, 22])
            returns True (since 8 * 2 is 16, and 8 comes before 16 in ints)
    Note from that last example, that there are two pairs of values where one
    is the double of the other (8, 16, and 14, 28), but only one such pair is
    required for the function to return True.

    Parameters:

        ints is a list of 0 or more integers.
        index is an in indicating an index position.  This parameter is optional.  The default is 0.
    """

    if len(ints) == 1 or len(ints) == 0:
        return False
    #if your data is 0 or 1 ints long, return False
    elif (ints[0] * 2) == ints[1]:
        #if current element times 2 equals adjacent, return True on the spot
        return True
    else:
        return find_double(ints[1:], index=0)
        #otherwise, move on to the next number

#Question #5


def Ashwany(n):
    """

    Ashwany is a firefighter and an athlete who likes to train by climbing ladders.
    There are many ladders of various lengths available at Ashwany's house and at the fire station.
    The longest of these has 30 rungs (cross pieces – the things you step on),
    and the shortest just one (a collapsible stepping stool Ashwany has at home for reaching upper shelves).

    For exercise, Ashwany likes to climb ladders one, two, or three rungs at a time.
    Write and test a Python 3 function called climbing_patterns_count() for Ashwany that takes one integer argument,
    representing a number of rungs, and returns another integer representing the number of possible patterns of climbing a ladder with that number of rungs.

    For example,

    climbing_patterns_count(1) returns 1
    climbing_patterns_count(2) returns 2 (because Ashwany can take two single steps or one double step up a two-rung ladder)
    climbing_patterns_count(3) returns 4 (three single steps, a double and a single, a single and a double, or all three at once)
    climbing_patterns_count(4) returns 7 (and you get to confirm that for yourself!)
    """

    if n == 1 or n == 0:
        #if the value is 1 or 0, then the return value is 1 because there is only 1 possible way for him to go up ladder
        return 1
    elif n == 2:
        #if the value 2, then there are only 2 ways to go up ladder, because "because Ashwany can take two single steps or one double step up a two-rung ladder"
        return 2

    else:
        return Ashwany(n-3) + Ashwany(n-2) + Ashwany(n-1)
        #count the three ways to climb up the stairs every time by calling it recursively 3 stairs down each time




if __name__ == "__main__":
    print("Testing Question 1")
    print(split_int_pairs([]))
    print(split_int_pairs([-5]))
    print(split_int_pairs([-5, 1]))
    print(split_int_pairs([-5, -5]))
    print(split_int_pairs([0, 1, 0, 1, 1, 0, 0]), "\n")

    print("Testing Question 2")
    print(count_split_char_pairs(""))
    print(count_split_char_pairs("aA"))
    print(count_split_char_pairs("aAa"))
    print(count_split_char_pairs("bAbA"))
    print(count_split_char_pairs("BcBcBc"), "\n")

    print("Testing Question 3")
    print(check_nesting(""))
    print(check_nesting("["))
    print(check_nesting("[]"))
    print(check_nesting("[]]"))
    print(check_nesting("[[]]"))
    print(check_nesting("[[[[[[[[[]]]]]]]]]"), "\n")

    print("Testing Question 4")
    print(find_double([]))
    print(find_double([3]))
    print(find_double([3, 5]))
    print(find_double([3, 5, 6]))
    print(find_double([3, 6]))
    print(find_double([7, 8, 16, 15, 3, 22]))
    print(find_double([7, 8, 16, 14, 28, 22]), "\n")

    print("Testing Question 5")
    print(Ashwany(1))
    print(Ashwany(2))
    print(Ashwany(3))
    print(Ashwany(4))
    print(Ashwany(5))
    print(Ashwany(6))
    print(Ashwany(7))
    print(Ashwany(8), "\n")




