"""
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
Submitted on: Nov. 25
"""
    
def userinput():
    try:
        numlist = input("Please enter a maximum of four numbers \"with spaces\" to sort them: ")
        numlist = numlist.split(" ")
        # print(numlist) # Check values.    
        numlist = [int(num) for num in numlist if num != ""]
        print(numlist)
    except IndexError as e:
        print("IndexError")
    
    # print(numlist) # To check values.
    return numlist
# End of function.

def numsorter(sort_list):
    try:
        num_1, num_2, num_3, num_4 = [i for i in sort_list]
    except ValueError as e:
        print("You entered incorrectly. Try again.")
        
    # Trying 24 combinations of a set of 4 elements.
    
    if num_1 > num_2 > num_3 > num_4:
        num_1, num_2, num_3, num_4 = num_1, num_2, num_3, num_4
    elif num_1 > num_2 > num_4 > num_3:
        num_1, num_2, num_3, num_4 = num_1, num_2, num_4, num_3
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_1 > num_3 > num_2 > num_4:
        num_1, num_2, num_3, num_4 = num_1, num_3, num_2, num_4
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_1 > num_3 > num_4 > num_2:
        num_1, num_2, num_3, num_4 = num_1, num_3, num_4, num_2
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_1 > num_4 > num_2 > num_3:
        num_1, num_2, num_3, num_4 = num_1, num_4, num_2, num_3
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_1 > num_4 > num_3 > num_2:
        num_1, num_2, num_3, num_4 = num_1, num_4, num_3, num_2
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_2 > num_1 > num_3 > num_4:
        num_1, num_2, num_3, num_4 = num_2, num_1, num_3, num_4
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_2 > num_1 > num_4 > num_3:
        num_1, num_2, num_3, num_4 = num_2, num_1, num_4, num_3
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_2 > num_3 > num_4 > num_1:
        num_1, num_2, num_3, num_4 = num_2, num_3, num_4, num_1
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_2 > num_3 > num_1 > num_4:
        num_1, num_2, num_3, num_4 = num_2, num_3, num_1, num_4
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_2 > num_4 > num_1 > num_3:
        num_1, num_2, num_3, num_4 = num_2, num_4, num_1, num_3
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_2 > num_4 > num_3 > num_1:
        num_1, num_2, num_3, num_4 = num_2, num_4, num_3, num_1
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_3 > num_1 > num_2 > num_4:
        num_1, num_2, num_3, num_4 = num_3, num_1, num_2, num_4
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_3 > num_1 > num_4 > num_2:
        num_1, num_2, num_3, num_4 = num_3, num_1, num_4, num_2
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_3 > num_2 > num_1 > num_4:
        num_1, num_2, num_3, num_4 = num_3, num_2, num_1, num_4
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_3 > num_2 > num_4 > num_1:
        num_1, num_2, num_3, num_4 = num_3, num_2, num_4, num_1
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_3 > num_4 > num_1 > num_2:
        num_1, num_2, num_3, num_4 = num_3, num_4, num_1, num_2
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_3 > num_4 > num_2 > num_1:
        num_1, num_2, num_3, num_4 = num_3, num_4, num_2, num_1
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_4 > num_1 > num_2 > num_3:
        num_1, num_2, num_3, num_4 = num_4, num_1, num_2, num_3
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_4 > num_1 > num_3 > num_2:
        num_1, num_2, num_3, num_4 = num_4, num_1, num_3, num_2
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_4 > num_2 > num_1 > num_3:
        num_1, num_2, num_3, num_4 = num_4, num_2, num_1, num_3
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_4 > num_2 > num_3 > num_1:
        num_1, num_2, num_3, num_4 = num_4, num_2, num_3, num_1
        print("sorted",num_1,num_2,num_3,num_4)
    elif num_4 > num_3 > num_1 > num_2:
        num_1, num_2, num_3, num_4 = num_4, num_3, num_1, num_2
    else:
        return [num_4, num_3, num_2, num_1]
    return [num_1, num_2, num_3, num_4]
# End of function.


def display(unsort_list, sort_list): # Prints the grade in format.
    
    print(
    """
    The unsorted list: {0}
    Sorted from highest to lowest: {1}
    """.format(unsort_list, sort_list)
    )
# End of Func.

def main():
    unsort_list = userinput()
    sorted_list = numsorter(unsort_list)
    display(unsort_list, sorted_list)
# End of function.

while True: # My template for usual main().
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
        print(quit)
    if (quit == 'y' or quit == 0):
        print("Closing...\n")    
        break
# End of Func.

exit() # Exits program.