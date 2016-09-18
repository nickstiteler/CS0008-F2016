#
# Template for code submission
# name       : Nicholas Stiteler
# email      : njs74@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Day of the week
# Example: Starting with Python, Chapter 3, Exercise 1
3
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# Enter Input
number = input("Enter a number 1-7_")

# I test
number = int(number)

# Testing if input is within the range of 1-7
if(number>7 or number<1):
    print("Error! Number must be between 1 and 7")
    exit

# if and elif statements for printing of the days of the week
elif(number==1):
    print("Monday")
elif(number==2):
    print("Tuesday")
elif(number==3):
    print("Wednesday")
elif(number==4):
    print("Thursday")
elif(number==5):
    print('Friday')
elif(number==6):
    print('Saturday')
elif(number==7):
    print('Sunday')