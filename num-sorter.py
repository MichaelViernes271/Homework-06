"""
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
Submitted on: Nov. 25
"""
    
def userinput():

    numlist = input("Please enter a maximum of four numbers \"with spaces\" to sort them: ")
    numlist = numlist.split(" ")
    # print(numlist) # Check values.    
    numlist = [int(num) for num in numlist if num != ""]
    
    # print(numlist) # Check values.
    return numlist
# End of function.

