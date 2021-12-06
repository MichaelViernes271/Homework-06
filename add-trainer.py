"""
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

import random

num_of_pts = 0

for i in range(10): # Loop quesetions
    addend_x = random.randint(0, 100)
    addend_y = random.randint(0, 100)
    sum = addend_x + addend_y
    print(f"{i+1}. Solve: {addend_x} + {addend_y}?")
    try:
        answer = int(input("Your answer: "))
    except:
        print("\nEnter a  correct value.\n")
    if (answer == sum):
        print(f"Correct: {addend_x} + {addend_y} = {sum}")
        num_of_pts += 1
    else: print(f"Incorrect: {addend_x} + {addend_y} = {sum}")
    if i == 9:
        print(f"\nResults: {num_of_pts}/10\n")
        break
        