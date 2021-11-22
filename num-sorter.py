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
        a, b, c, d = [i for i in sort_list]
    except ValueError as e:
        print("You entered incorrectly. Try again.")
        
    # Trying 24 combinations of a set of 4 elements.
    
    if a > b > c > d:
        a, b, c, d = a, b, c, d
    elif a > b > d > c:
        a, b, c, d = a, b, d, c
        print("sorted",a,b,c,d)
    elif a > c > b > d:
        a, b, c, d = a, c, b, d
        print("sorted",a,b,c,d)
    elif a > c > d > b:
        a, b, c, d = a, c, d, b
        print("sorted",a,b,c,d)
    elif a > d > b > c:
        a, b, c, d = a, d, b, c
        print("sorted",a,b,c,d)
    elif a > d > c > b:
        a, b, c, d = a, d, c, b
        print("sorted",a,b,c,d)
    elif b > a > c > d:
        a, b, c, d = b, a, c, d
        print("sorted",a,b,c,d)
    elif b > a > d > c:
        a, b, c, d = b, a, d, c
        print("sorted",a,b,c,d)
    elif b > c > d > a:
        a, b, c, d = b, c, d, a
        print("sorted",a,b,c,d)
    elif b > c > a > d:
        a, b, c, d = b, c, a, d
        print("sorted",a,b,c,d)
    elif b > d > a > c:
        a, b, c, d = b, d, a, c
        print("sorted",a,b,c,d)
    elif b > d > c > a:
        a, b, c, d = b, d, c, a
        print("sorted",a,b,c,d)
    elif c > a > b > d:
        a, b, c, d = c, a, b, d
        print("sorted",a,b,c,d)
    elif c > a > d > b:
        a, b, c, d = c, a, d, b
        print("sorted",a,b,c,d)
    elif c > b > a > d:
        a, b, c, d = c, b, a, d
        print("sorted",a,b,c,d)
    elif c > b > d > a:
        a, b, c, d = c, b, d, a
        print("sorted",a,b,c,d)
    elif c > d > a > b:
        a, b, c, d = c, d, a, b
        print("sorted",a,b,c,d)
    elif c > d > b > a:
        a, b, c, d = c, d, b, a
        print("sorted",a,b,c,d)
    elif d > a > b > c:
        a, b, c, d = d, a, b, c
        print("sorted",a,b,c,d)
    elif d > a > c > b:
        a, b, c, d = d, a, c, b
        print("sorted",a,b,c,d)
    elif d > b > a > c:
        a, b, c, d = d, b, a, c
        print("sorted",a,b,c,d)
    elif d > b > c > a:
        a, b, c, d = d, b, c, a
        print("sorted",a,b,c,d)
    elif d > c > a > b:
        a, b, c, d = d, c, a, b
    else:
        return True
    return [a, b, c, d]
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