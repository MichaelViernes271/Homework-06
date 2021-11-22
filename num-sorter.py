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

def numsorter(sort_list):
    try:
        a, b, c, d = [i for i in sort_list]
    except ValueError as e:
        print("You entered incorrectly. Try again.")
        
    # Trying 24 combinations of a set of 4 elements.
    
    if a > b > c > d:
        d, c, b, a = a, b, c, d
    elif a > b > d > c:
        d, c, b, a = a, b, d, c
        print("sorted",a,b,c,d)
    elif a > c > b > d:
        d, c, b, a = a, c, b, d
        print("sorted",a,b,c,d)
    elif a > c > d > b:
        d, c, b, a = a, c, d, b
        print("sorted",a,b,c,d)
    elif a > d > b > c:
        d, c, b, a = a, d, b, c
        print("sorted",a,b,c,d)
    elif a > d > c > b:
        d, c, b, a = a, d, c, b
        print("sorted",a,b,c,d)
    elif b > a > c > d:
        d, c, b, a = b, a, c, d
        print("sorted",a,b,c,d)
    elif b > a > d > c:
        d, c, b, a = b, a, d, c
        print("sorted",a,b,c,d)
    elif b > c > d > a:
        d, c, b, a = b, c, d, a
        print("sorted",a,b,c,d)
    elif b > c > a > d:
        d, c, b, a = b, c, a, d
        print("sorted",a,b,c,d)
    elif b > d > a > c:
        d, c, b, a = b, d, a, c
        print("sorted",a,b,c,d)
    elif b > d > c > a:
        d, c, b, a = b, d, c, a
        print("sorted",a,b,c,d)
    elif c > a > b > d:
        d, c, b, a = c, a, b, d
        print("sorted",a,b,c,d)
    elif c > a > d > b:
        d, c, b, a = c, a, d, b
        print("sorted",a,b,c,d)
    elif c > b > a > d:
        d, c, b, a = c, b, a, d
        print("sorted",a,b,c,d)
    elif c > b > d > a:
        d, c, b, a = c, b, d, a
        print("sorted",a,b,c,d)
    elif c > d > a > b:
        d, c, b, a = c, d, a, b
        print("sorted",a,b,c,d)
    elif c > d > b > a:
        d, c, b, a = c, d, b, a
        print("sorted",a,b,c,d)
    elif d > a > b > c:
        d, c, b, a = d, a, b, c
        print("sorted",a,b,c,d)
    elif d > a > c > b:
        d, c, b, a = d, a, c, b
        print("sorted",a,b,c,d)
    elif d > b > a > c:
        d, c, b, a = d, b, a, c
        print("sorted",a,b,c,d)
    elif d > b > c > a:
        d, c, b, a = d, b, c, a
        print("sorted",a,b,c,d)
    elif d > c > a > b:
        d, c, b, a = d, c, a, b
    else:
        return True
    return [a, b, c, d]
# End of function.


def display(unsort_list, sort_list): # Prints the grade in format.
    
    print(
    """
    The unsorted list: {0}
    The sorted list: {1}
    """.format(unsort_list, sort_list)
    )
# End of Func.

def main():
    unsort_list = userinput()
    sorted_list = numsorter(unsort_list)
    if sorted_list == True:
        print(f"The list {unsort_list} is already sorted.")
        return
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