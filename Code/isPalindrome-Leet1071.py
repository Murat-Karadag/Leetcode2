def isPalindrome(x: int) -> bool:

    # Number is negative: Return False
    if x < 0:
        return False

   # Init a list, make the number a string, initialiase a running-variable
   # and an index n to get the characters of the number x

    testlist = []
    lenge = len(str(x))
    laufvariable = 0
    n = 0

    # Always append the end first
    while lenge > laufvariable:
        n -= 1
        testlist.append(str(x)[n])
        laufvariable +=1

    # If while-loop finished make the list to a string via join
    to_return_string = "".join(testlist)

    return to_return_string == str(x)

    # if to_return_string == str(x):
    #    return True
    # else:
    #    return False


x = 1212
print(isPalindrome(x))


