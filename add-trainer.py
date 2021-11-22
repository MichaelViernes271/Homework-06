"""
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

import random

num_of_pts = 0

for i in range(10): # Loop quesetions
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    sum = x + y
    print(f"{i+1}. Solve: {x} + {y}?")
    try:
        ans = int(input("Your answer: "))
    except:
        print("\nEnter a  correct value.\n")
    if (ans == sum):
        print(f"Correct: {x} + {y} = {sum}")
        num_of_pts += 1
    else: print(f"Incorrect: {x} + {y} = {sum}")
    if i == 9:
        print(f"\nResults: {num_of_pts}/10\n")
        break
        