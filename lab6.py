# your full name (as it appears in Blackboard)
# your 9-digit SBU ID number
# Your Stony Brook NetID (Blackboard username)
# CSE 101
# Lab 6

import string

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def signature(name):
    # ADD YOUR CODE HERE
    return "" # CHANGE OR REPLACE THIS LINE


def oddRuns(sequence):
    # ADD YOUR CODE HERE
    return -1 # CHANGE OR REPLACE THIS LINE


def lol(level):
    # ADD YOUR CODE HERE
    return "" # CHANGE OR REPLACE THIS LINE


def pattern(n):
    # ADD YOUR CODE HERE
    return "" # CHANGE OR REPLACE THIS LINE


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing signature("uther"):', signature("uther"))

    print('Testing signature("essaul"):', signature("essaul"))

    print('Testing signature("maerl4n"):', signature("maerl4n"))

    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing oddRuns("0101110000"):', oddRuns("0101110000"))

    print('Testing oddRuns("001001110010000"):', oddRuns("001001110010000"))

    print('Testing oddRuns("10001011011011100011"):', oddRuns("10001011011011100011"))

    # Write your own tests for Part 2 here!
    print() # prints a blank line

    ############### Part 3 Tests ###############
    print('Testing lol(0):', lol(0))

    print('Testing lol(2):', lol(2))

    print('Testing lol(5):', lol(5))

    # Write your own tests for Part 3 here!
    print()  # prints a blank line

    ############### Part 4 Tests ###############
    print('pattern(1) prints', pattern(1))

    print('pattern(3) prints', pattern(3))

    print('pattern(5) prints', pattern(5))

    # Write your own tests for Part 4 here!
    print()  # prints a blank line


